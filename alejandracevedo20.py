from instapy import InstaPy
from instapy import smart_run

#.strip().lower()

# login credentials

insta_username = 'alejandracevedo20'
insta_password = '604030755ALEJA'

#restriction DATA

#target DATA

targets = {
    'nataliareyesg', 'kimberly.loaiza', 'aalessaronda', 'mariapedraza_', 'yuyacst', 'benefitcosmetics', 'yellabella', 'melinaramirez90', 'pautips', 'rihannafanpage', 'karolg'
}

#ignore-targets = {}

#locations DATA

locations = {'567077758/mexico/', '669811849726034/cdmx/'
}

#ignore-locations = {}

#hashtags DATA

hashtags = {
    'makeup', 'makeupartist', 'beauty', 'mexico', 'cdmx', 'colombian', 'colombiana', 'morenaza', 'morena', 'model', 'mexicocity', 'cdmx', 'ciudaddemexico', 'mexicourbano', 'mexinstantes', 'mexicodf', 'df', 'instacdmx', 'cdmx'   
}

#ignore-hashtags = {}

#word DATA

ignore_words = {
    'free shipping', ' Order', 'visa', 'paypal', 'envio gratis', 'master card', 'tienda', 'cannabis', 'bullfight'
}

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True,
                  disable_image_load=True,
                bypass_security_challenge_using='email')

# let's go! :>
with smart_run(session):
    
# general settings
    
#Estos son los parametros para decidir si interactuar con ellos o no 

    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    min_followers=150,
                                    min_following=30,
                                    min_posts=5)

#Estos parametros se usan para no interactuar con usuarios en base a si esta privado elperfil, si tienen foto de perfil, si es cuenta business, o si tienen palabras que no queremos    
    
    session.set_skip_users(skip_private=True,
                       private_percentage=100,
                       skip_no_profile_pic=True,
                       no_profile_pic_percentage=100,
                       skip_business=False,
		              skip_non_business=False,
                       business_percentage=100,
                        skip_bio_keyword = ignore_words)
    

#Este parametro hace que el tiempo entre like y like sea al azar, los rangos son porcentajes en base al tiempo que pusimos en like.

    session.set_action_delays(enabled=True,
                              like=5.2,
                              randomize=True,
                              random_range_from=70,
                              random_range_to=140)
    
    
# Interact with the people that a given user is followed by

# set_user_interact: Amount se refiere a la cantidad de posts, randomize es si al azar o no, percentage es el porcentaje del total de los nuevos a los que sigues, media es photo o video
# set_do_comment, set_do_follow and set_do_like are applicable
# set_do_like method is only needed for the interact_by_... actions. Posts will be liked by default when using like_by_... actions.
# set_do_follow method default enabled=False, follows ~ 10% of the users from the images, times=1
# (only follows a user once (if unfollowed again)

    session.set_user_interact(amount=5, randomize=True, percentage=100, media='Photo')
    session.set_do_follow(enabled=True, percentage=70)
    session.set_do_like(enabled=True, percentage=70)
    #session.interact_user_followers(targets, amount=10, randomize=True)
    #session.set_simulation(enabled=True, percentage=66)
    
# Prevents unfollow followers who have liked one of your latest X posts, only use when you are unfollowing ALL your followers

    #session.set_dont_unfollow_active_users(enabled=True, posts=30)    
    
# Generate smart hashtags based on https://displaypurposes.com ranking,
# banned and spammy tags are filtered out.
# (limit) defines amount limit of generated hashtags by hashtag
# (sort) sort generated hashtag list 'top' and 'random' are available
# (log_tags) shows generated hashtags before use it
# (use_smart_hashtags) activates like_by_tag to use smart hashtags

    #session.set_smart_hashtags(hashtags, limit=3, sort='top', log_tags=True)
    
    #session.set_smart_location_hashtags(locations, radius=20, limit=10)
    
    
#Activity    


# follow activity

    amount_number = 30    
    
#Le da follow a los usuarios de las cuentas que escogemos

    session.follow_user_followers(targets, amount=30, randomize=True, interact=True, sleep_delay=60)
    
# Follow user based on hashtags (without liking the image)

    session.follow_by_tags(hashtags, amount=30, use_smart_hashtags=False, use_smart_location_hashtags=False, randomize=True, interact=True)
    
#Follow basado en la location    
    
    session.follow_by_locations(locations, amount=30)

#Follow a los que le commentan a tus targets

    #session.follow_commenters([targets], amount=3, daysold=15, max_pic = 5, interact=True)

    
    

#like activity

#Like posts based on hashtags, the amount is per tag    
    session.like_by_tags(hashtags, amount=10, use_smart_hashtags=False, use_smart_location_hashtags=False, skip_top_posts=True, interact=True)

# Like a posts basado en su ubicacion
    session.like_by_locations(locations, amount=20)
    

    
    
    
# unfollow activity


# Le da unfollow a los que no te siguen de regreso y solo son de los que empezaste a seguir usando InstaPy. Usa 'all' para dejar de seguir a todos los que instapy siguio.
#unfollow_after - el tiempo es en segundos. By using this, you can unfollow users only after following them certain amount of time.
   
    session.unfollow_users(amount=300, instapy_followed_enabled=True, instapy_followed_param="nonfollowers", style="FIFO", unfollow_after=96 * 60 * 60, sleep_delay=300)

#Le da unfollow a todos los que no te siguen, independientemente de como empezaste a seguirlos

    #session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=300)
    
#Le da unfollow a todos, sin importar si te siguen o no, ni como los empezaste a seguir.    
    
    #session.unfollow_users(amount=40, allFollowing=True, style="LIFO", unfollow_after=3*60*60, sleep_delay=300)

    #""" Joining Engagement Pods...
    #"""
   # session.join_pods(topic='fashion', engagement_mode='no_comments')
    