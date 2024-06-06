# from django.contrib import admin
# from .models import History_events, History_events_fails,History_prices

# class HistoryEventsAdmin(admin.ModelAdmin):
#     list_display = ['id_event', 'fk_imagetrack', 'date','delete_soft','status_scan'] 
#     list_filter = ['id_event', 'fk_imagetrack', 'date','delete_soft','status_scan']
    
# class HistoryEventsFailAdmin(admin.ModelAdmin):
#     list_display = ['id_history_events_fails', 'fk_history_events','delete_soft']
#     list_filter = ['id_history_events_fails', 'fk_history_events','delete_soft']  

# class HistoryPricesAdmin(admin.ModelAdmin):
#     list_display = ['id_history_prices', 'fk_history_events', 'price_scan','delete_soft']
#     list_display = ['id_history_prices', 'fk_history_events', 'price_scan','delete_soft']   
     

# admin.site.register(History_events,HistoryEventsAdmin)
# admin.site.register(History_events_fails, HistoryEventsFailAdmin)
# admin.site.register(History_prices, HistoryPricesAdmin)

