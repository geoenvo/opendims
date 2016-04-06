import os
import django
import psycopg2


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opendims.settings")
django.setup()


from geolevels.models import Province, City, Subdistrict, Village, RW, RT


if __name__ == '__main__':
    conn = psycopg2.connect(
        "host='localhost' dbname='geolevels' user ='vagrant' password='password'"
    )
    cur = conn.cursor()
    sql_prov = "SELECT * FROM boundary_prov;"
    cur.execute(sql_prov)
    rows = cur.fetchall()
    list_prov = [
        Province(id=row[3], name=row[2], polygon=row[1]) for row in rows
    ]

    for prov in list_prov:
        if not prov.name:
            prov.name = ''
        print prov.id, prov.name
        prov.save()
        cur2 = conn.cursor()
        sql_city = "SELECT * FROM boundary_kab WHERE id_prov = %d" % prov.id
        cur2.execute(sql_city)
        rows_city = cur2.fetchall()
        list_city = [
            City(
                id=row_city[4],
                name=row_city[2],
                polygon=row_city[1],
                province=prov
            ) for row_city in rows_city
        ]

        for city in list_city:
            if not city.name:
                city.name = ''
            print city.id, city.name
            city.save()
            cur3 = conn.cursor()
            sql_subdistrict = (
                "SELECT * FROM boundary_kec WHERE id_kab= %d" % city.id
            )
            cur3.execute(sql_subdistrict)
            rows_subdistrict = cur3.fetchall()
            list_subdistrict = [
                Subdistrict(
                    id=row_subdistrict[5],
                    name=row_subdistrict[2],
                    polygon=row_subdistrict[1],
                    city=city
                ) for row_subdistrict in rows_subdistrict
            ]

            for subdistrict in list_subdistrict:
                if not subdistrict.name:
                    subdistrict.name = ''
                print subdistrict.id, subdistrict.name
                subdistrict.save()
                cur4 = conn.cursor()
                sql_village = (
                    "SELECT * FROM boundary_kel WHERE id_kec= %d"
                    % subdistrict.id
                )
                cur4.execute(sql_village)
                rows_village = cur4.fetchall()
                list_village = [
                    Village(
                        id=row_village[2],
                        name=row_village[3],
                        polygon=row_village[1],
                        subdistrict=subdistrict
                    ) for row_village in rows_village
                ]

                for village in list_village:
                    if not village.name:
                        village.name = ''
                    print village.id, village.name
                    village.save()
                    cur5 = conn.cursor()
                    sql_rw = (
                        "SELECT * FROM boundary WHERE id_kel= '%s'"
                        % village.id
                    )
                    cur5.execute(sql_rw)
                    rows_rw = cur5.fetchall()
                    list_rw = [
                        RW(
                            id=row_rw[7],
                            name=row_rw[5],
                            polygon=row_rw[1],
                            village=village
                        ) for row_rw in rows_rw
                    ]

                    for rw in list_rw:
                        if not rw.name:
                            # print 'NULL FOUND'
                            rw_id = str(rw.id)
                            rw.name = rw_id[10:13]
                        print rw.id, rw.name
                        rw.save()
                        cur6 = conn.cursor()
                        sql_rt = (
                            "SELECT * FROM boundary_rt WHERE id_rw= '%s'"
                            % rw.id
                        )
                        cur6.execute(sql_rt)
                        rows_rt = cur6.fetchall()
                        list_rt = [
                            RT(
                                id=row_rt[4],
                                name=row_rt[11],
                                polygon=row_rt[1],
                                rw=rw
                            ) for row_rt in rows_rt
                        ]

                        for rt in list_rt:
                            if not rt.name:
                                print 'NULL RT FOUND'
                                rt_id = str(rt.id)
                                rt.name = rt_id[13:]
                            print rt.id, rt.name
                            rt.save()
