from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    help = "FTP 服务器"

    def add_arguments(self, parser: CommandParser):
        super().add_arguments(parser)

    def handle(self, *args, **options):
        """
        处理实时获取订单
        """
        pass
