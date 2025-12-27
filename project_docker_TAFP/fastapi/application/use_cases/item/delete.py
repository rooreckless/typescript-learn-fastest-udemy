"""
商品削除ユースケース
"""

from application.services.item_service import ItemService


class DeleteItemUseCase:
    """商品削除ユースケース"""

    def __init__(self, item_service: ItemService):
        """
        Args:
            item_service: 商品サービス
        """
        self.item_service = item_service

    async def __call__(
        self,
        item_id: int
    ) -> bool:
        """
        商品を論理削除する
        
        Args:
            item_id: 商品ID
            
        Returns:
            削除が成功した場合True、失敗した場合False
        """
        target_item = await self.item_service.get_item_by_id(item_id)
        if not target_item:
            return None
        # 商品を削除
        success = await self.item_service.delete_item(target_item)
        
        return success
