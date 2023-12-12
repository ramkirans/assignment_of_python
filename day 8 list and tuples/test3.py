#to add or remove an element from the list use append and remove function as shown below
#to add
s3_bucket_lists = ["ram_demo_bucket", "lee_demo_bucket", "bale_demo_bucket", "jam_demo_bucket"]
s3_bucket_lists.append("new_s3_bucket")  #variable.function("new_element")
print(s3_bucket_lists)

#to remove
s3_bucket_lists = ["ram_demo_bucket", "lee_demo_bucket", "bale_demo_bucket", "jam_demo_bucket", "new_s3_bucket"]
s3_bucket_lists.remove("new_s3_bucket")  #variable.function("remove_element")
print(s3_bucket_lists)

