import { Component,inject,signal,NgModule } from '@angular/core';
import { AsyncPipe } from '@angular/common';
import { CategoryService } from '../services/category';
import { Subject, of} from 'rxjs';
import { switchMap, map, catchError, startWith } from 'rxjs/operators';
import { FormsModule } from '@angular/forms';
import { HttpErrorResponse } from '@angular/common/http';

type SubmitState =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success' }
  | { status: 'error'; message: string; code?: number };


@Component({
  selector: 'app-category-form',
  imports:[FormsModule,AsyncPipe],
  templateUrl: './category-form.html',
  styleUrl: './category-form.css',
})
export class CategoryForm {
    // // fb = FormBuilderのインスタンス、はフォームの構造を定義するための準備
    // private fb = inject(FormBuilder);
    
    // 送信トリガー(この段階ではただのObservableの後で呼ばれる予定の、Subjectのインスタンスであると宣言しただけ)
    private submit$ = new Subject<any>();


    // ⭐ async pipe 用 Observable
    // submit$の中で、switchMapでPOSTを実行し、その結果をstate$が受け取る
    // が、今の段階ではただの準備段階。onSubmitでsubmit$.next()を呼び出す必要がある
    state$ = this.submit$.pipe(
      // ↑のpipe内で、submit$がnextされたときに実行される処理を定義。
      // 「pipe内のものが順番に実行される」のでswithMapの後にstartWithが実行される形。
      // ↓switchMapの引数な無名関数で「formValueの内容でPOSTリクエストをcategoryService.createCategory」で実行。その後にpipeがついているので、
      // さらにその中でmap, startWith, catchErrorが順番に実行される
      // そもそも、swithMapはObservableを返す関数を引数に取るので、categoryService.createCategory(formValue)がObservableを返す必要がある
      // また、swithMapは連打されたら前のリクエストをキャンセルする効果もある
      switchMap((formValue) =>
        this.categoryService.createCategory(formValue).pipe(
          //mapでは、POSTが成功した時の表示用データを作っている(まだこの段階では結果を受け取っていない)
          map((): SubmitState => ({ status: 'success' })),
          // startWithでは、POSTリクエストが始まった直後にloadingステータスを返す
          startWith<SubmitState>({ status: 'loading' }),
          // catchErrorでは、POSTが失敗した時用のエラーステータスとメッセージを準備する
          // ofでObservableに変換して返す必要がある
          catchError((err: unknown) => {
            const message = this.toMessage(err);
            return of<SubmitState>({ status: 'error', message, code: this.toStatus(err) });
          })
        )
      ),
      // 初期状態としてidleステータスを返すための準備(送信ボタンを押す前のloading状態時のため)
      startWith<SubmitState>({ status: 'idle' })
    );
    // フォームの内容をPOSTするためのCategoryServiceを注入
    constructor(private categoryService :CategoryService){}
    

    // 送信ボタンが押されたときに呼び出されるメソッド。これでpost処理が始まり、state$が更新される
    onSubmit(formValue: any) {
      this.submit$.next(formValue);
    }
    // switchMapでエラーステータスコードを返す。ここで作成したものがonSubmit実行時にswitchMapに渡される
    private toStatus(err: unknown): number | undefined {
      return err instanceof HttpErrorResponse ? err.status : undefined;
    }
    // switchMapでエラーステータスコードに応じたメッセージを返す。ここで作成したものがonSubmit実行時にswitchMapに渡される
    private toMessage(err: unknown): string {
      if (err instanceof HttpErrorResponse) {
        // FastAPI が detail を返すことが多い
        const detail = (err.error && (err.error.detail ?? err.error.message)) || null;

        if (err.status === 401) return 'ログインしてください（認証が必要です）。';
        if (err.status === 403) return '権限がありません（admin でログインしてください）。';
        if (typeof detail === 'string') return detail;
        return `送信に失敗しました（HTTP ${err.status}）`;
      }
      return '送信に失敗しました。';
    }
}
