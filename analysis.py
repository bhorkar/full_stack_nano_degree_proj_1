#!/usr/bin/env python3


import psycopg2


def perform_query(cur, sql, explanation='views'):
    cur.execute(sql)
    row = [item for item in cur.fetchall()]
    for r in row:
        print("{}--{} {}".format(r[0], r[1], explanation))
    print("**************************")


def main():
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()

# Q1
    print("1. What are the most popular three articles of all time?")
    sql_query = """
                 select title, count(*) as view_count
                 from log join articles
                 on articles.slug = SPLIT_PART(log.path,'/',3)
                 group by title
                 order by view_count desc
                 limit 3;
                """
    perform_query(cur, sql_query)
# Q2
    print("2. Who are the most popular article authors of all time? ")
    sql_query = """
                  select name, count(*) as view_count
                  from (authors join articles
                  on authors.id = articles.author)
                  join log
                  on articles.slug = SPLIT_PART(log.path,'/',3)
                  group by name
                  order by view_count desc;
                """
    perform_query(cur, sql_query)
# Q3
    print("3. On which days did more than 1% of requests lead to errors?")
    sql_query = """
       select to_char(date,'MON DD YYYY'), err/total*100 as ratio
       from (select cast(time as date) as date,
                    count(*) as total,
                    cast(sum(cast((status not like '200 OK') as int)) as float)
                    as err
                    from log
                    group by date) as errors
       where err/total > 0.01;

    """
    perform_query(cur, sql_query, '% errors')


if __name__ == "__main__":
    main()
