from rest_framework import serializers
from  .models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WatchList
        fields = '__all__'
#end class

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchList(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        