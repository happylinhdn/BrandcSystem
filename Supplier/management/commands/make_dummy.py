from django.core.management.base import BaseCommand, CommandError
from Supplier.models import Supplier, DummyModel

class Command(BaseCommand):
    help = 'Make dummy item'
        
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('call Make dummy item'))
        count = Supplier.objects.count()
        self.stdout.write(self.style.SUCCESS('All Supplier is "%s"' % count))
        all_suppliers = Supplier.objects.all().order_by('id')
        
        for supplier in all_suppliers:
            print(supplier.id)
            item = DummyModel(
                name = supplier.name,
                link = supplier.link,
                channel = supplier.channel,
                follower = supplier.follower,
                follower_2 = supplier.follower_2,
                kol_tier = supplier.kol_tier,
                engagement_rate_percent = supplier.engagement_rate_percent,
                engagement_rate_absolute = supplier.engagement_rate_absolute,
                location = supplier.location,
                year_of_birth = supplier.year_of_birth,
                gender = supplier.gender,
                industries = supplier.industries,
                original_cost_picture = supplier.original_cost_picture,
                original_cost_video = supplier.original_cost_video,
                original_cost_event = supplier.original_cost_event,
                original_cost_tvc = supplier.original_cost_tvc,
                kpi = supplier.kpi,
                discount = supplier.discount,
                supplier_name = supplier.supplier_name,
                booking_contact_name = supplier.booking_contact_name,
                booking_contact_phone = supplier.booking_contact_phone,
                booking_contact_email = supplier.booking_contact_email,
                profile = supplier.profile,
                latest_update = supplier.latest_update,
                handle_by = supplier.handle_by,
                group_chat_name = supplier.group_chat_name,
                group_chat_channel = supplier.group_chat_channel,
                lana_leader = supplier.lana_leader,
                history = supplier.history,
                modified_by = supplier.modified_by

            )
            item.save()

