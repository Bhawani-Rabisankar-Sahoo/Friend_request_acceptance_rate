select * ,count(*) 
from fb_friend_requests
where (user_id_sender , user_id_receiver) in (select user_id_sender , user_id_receiver 
from fb_friend_requests
where action = 'accepted'
)
and action = 'sent'
group by date 