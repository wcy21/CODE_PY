def build_profile(first, last, **user_info):
    """用户信息字典"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

user_profile = build_profile('blue', 'dog',
                             age=20,
                             sex='male',
                             location='China',
                             field='computer', )
print(user_profile)
