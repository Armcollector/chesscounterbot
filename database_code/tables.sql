drop table if exists recorded_resets
create table recorded_resets
(
    submission varchar(20),
    comment varchar(20),
    submision_created_utc int,
    record_created_utc int,
    comment_created_utc int,
    submission_url varchar(200)
)


