"""
商品更新ユースケース
"""

from typing import Optional
from domain import ItemEntity
from application.services.item_service import ItemService


class UpdateItemUseCase:
    """商品更新ユースケース"""

    def __init__(self, item_service: ItemService):
        """
        Args:
            item_service: 商品サービス
        """
        self.item_service = item_service

    async def __call__(
        self,
        item_id: int,
        name: Optional[str] = None,
        description: Optional[str] = None,
        price: Optional[float] = None,
        updated_by: Optional[str] = None
    ) -> Optional[ItemEntity]:
        """
        商品を更新する
        
        Args:
            item_id: 商品ID
            name: 新しい商品名（オプション）
            description: 新しい商品説明（オプション）
            price: 新しい価格（オプション）
            updated_by: 更新者
            
        Returns:
            更新された商品エンティティ、存在しない場合はNone
        """
        # 商品を更新
        item = await self.item_service.update_item(
            item_id=item_id,
            name=name,
            description=description,
            price=price,
            updated_by=updated_by
        )
        
        return item
