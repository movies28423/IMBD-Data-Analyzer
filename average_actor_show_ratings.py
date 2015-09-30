#!/usr/bin/env python 

# Import the imdb package.
import imdb

src_tv_show = raw_input("What tv show?  ")
src_season, src_episode = raw_input('What season & episode? (separate by comma)  ').split(',')

# Create the object that will be used to access the IMDb's database.
ia = imdb.IMDb() # by default access the web.
movie_list = ia.search_movie(src_tv_show)  
movie = ia.get_movie(movie_list[0].movieID)
ia.update(movie, 'episodes')  

src_episode_list = [y + 1 for y in xrange(0, int(src_season))]

actor_rating_dict = {}

for season_num in src_episode_list:
    episode_num = 1

    while int(episode_num) in movie['episodes'][int(season_num)].keys():
        episode = ia.get_movie(movie['episodes'][int(season_num)][episode_num].movieID)

        if episode == None:
        	continue;

        episode_rating = episode['rating']
        for person in episode['cast']:
            if person['name'] in actor_rating_dict.keys():
                actor_rating_dict[person['name']].append(episode_rating)
            else:
                actor_rating_dict.update({person['name']:[episode_rating]})

        if season_num == len(src_episode_list) and episode_num == len(src_episode):
        	episode_num = max(movie['episodes'][int(season_num)].keys()) + 1
        else:
        	episode_num += 1

for actor, ratings in actor_rating_dict.items():
    print(actor + ": " + str(sum(ratings) / float(len(ratings))))
