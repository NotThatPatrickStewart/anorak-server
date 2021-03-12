import json

whiskey_data = open("whiskeys.json", "r")
whiskey_dict = json.loads(whiskey_data.read())
whiskeys = []
tags = []
whiskey_tags = []
comparables = []
whiskey_comparables = []
tag_id = 1
tag_whiskey_id = 1
comparable_id = 1
comparable_whiskey_id = 1
for whiskey in whiskey_dict["whiskeys"]:
    whiskey_info = {}
    whiskey_info["id"] = whiskey["id"]
    whiskey_info["title"] = whiskey["title"]
    whiskey_info["list_img_url"] = whiskey["list_img_url"]
    whiskey_info["region"] = whiskey["region"]
    whiskey_info["price"] = whiskey["price"]
    whiskeys.append(whiskey_info)
    
    for tag in whiskey["tags"]:
        tag_info = {}
        tag_info["title"] = tag["title"]
        tag_info["count"] = tag["count"]
        tag_info["normalized_count"] = tag["normalized_count"]
        tag_info["id"] = tag_id
        tag_whiskey = {}
        tag_whiskey["whiskey_id"] = whiskey["id"]
        tag_whiskey["tag_id"] = tag_id
        tag_whiskey["id"] = tag_whiskey_id
        tag_whiskey_id = tag_whiskey_id + 1
        tag_id = tag_id + 1
        tags.append(tag_info)
        whiskey_tags.append(tag_whiskey)

    for comparable in whiskey["comparables"]:
        comparable_info = {}
        comparable_info["id"] = comparable_id
        comparable_info["title"] = comparable["title"]
        comparable_info["list_img_url"] = comparable["list_img_url"]
        comparable_info["region"] = comparable["region"]
        comparable_info["price"] = comparable["price"]
        comparable_whiskey = {}
        comparable_whiskey["whiskey_id"] = whiskey["id"]
        comparable_whiskey["comparable_id"] = comparable_id
        comparable_whiskey["id"] = comparable_whiskey_id
        comparable_whiskey_id = comparable_whiskey_id + 1
        comparable_id = comparable_id + 1
        comparables.append(comparable_info)
        whiskey_comparables.append(comparable_whiskey)

whiskey_json = open("new_whiskeys.json", "w")
tags_json = open("new_tags.json", "w")
whiskey_tags_json = open("new_whiskey_tags.json", "w")
comparables_json = open("new_comparables.json", "w")
whiskey_comparables_json = open("new_whiskey_comparables.json", "w")

whiskey_json.write(json.dumps(whiskeys, sort_keys=True, indent=4))
tags_json.write(json.dumps(tags, sort_keys=True, indent=4))
whiskey_tags_json.write(json.dumps(whiskey_tags, sort_keys=True, indent=4))
comparables_json.write(json.dumps(comparables, sort_keys=True, indent=4))
whiskey_comparables_json.write(json.dumps(whiskey_comparables, sort_keys=True, indent=4))