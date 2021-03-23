SELECT
    w.title as Whiskey,
    t.title as Flavor,
    wt.normalized_count
    FROM anorakapi_whiskey as w
        JOIN anorakapi_whiskeytag as wt
        ON wt.whiskey_id = w.id
        JOIN anorakapi_tag as t
        ON t.id = wt.tag_id
    GROUP BY Whiskey;

--     def list(self, request):
--         """Handle GET requests to whiskeys resource

--         Returns:
--             Response -- JSON serialized list of whiskeys
--         """
--         # Get all whiskey records from the database
--         whiskeys = Whiskey.objects.raw("""
--             SELECT
--             w.title as Whiskey,
--             w.list_img_url as Image,
--             w.price,
--             w.region,
--             w.id
--             t.title as Flavor,
--             wt.normalized_count,
--             FROM anorakapi_whiskey as w
--                 JOIN anorakapi_whiskeytag as wt
--                 ON wt.whiskey_id = w.id
--                 JOIN anorakapi_tag as t
--                 ON t.id = wt.tag_id
--             GROUP BY Whiskey
--         """)
--         print(whiskeys[6].Flavor)
--         serializer = WhiskeySerializer(
--             whiskeys, many=True, context={'request': request})

--         # comparable = serializer.data
--         # for whiskey in comparable:
--         #     for tag in 

--         return Response(serializer.data)


-- class WhiskeySerializer(serializers.ModelSerializer):
--     """JSON serializer for whiskeys

--     Arguments:
--         serializer type
--     """
    
--     class Meta:
--         model = Whiskey
--         fields = ('id', 'title', 'list_img_url', 'region', 'price')
--         depth = 1


--   tags = Tag.objects.get(user=request.auth.user)
--         whiskeys = Whiskey.objects.all()

--         for whiskey in whiskeys:
--             whiskey.matched = None

--             try:
--                 WhiskeyTag.objects.get(whiskey=whiskey, tag=tag)
--                 whiskey.matched = True
--             except WhiskeyTag.DoesNotExist:
--                 whiskey.matched = False

--         whiskey = self.request.query_params.get('whiskey_id', None)
--         if whiskey is not None:
--             tag