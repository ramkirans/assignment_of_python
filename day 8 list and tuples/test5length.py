#to check length of elements use len function

s3_bucket_lists = ["ram_demo_bucket", "lee_demo_bucket", "bale_demo_bucket", "jam_demo_bucket"]
print(len(s3_bucket_lists))

#appending new element to check len
s3_bucket_lists.append("new_s3_bucket")
print(len(s3_bucket_lists))

#removing an element to check
s3_bucket_lists.remove("lee_demo_bucket")
print(len(s3_bucket_lists))

#len function in tuple
s3_bucket_lists = ("ram_demo_bucket", "lee_demo_bucket", "bale_demo_bucket", "jam_demo_bucket")
print(len(s3_bucket_lists))