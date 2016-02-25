import os
import django
import psycopg2


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opendims.settings")
django.setup()


from geolevels.models import Province, City, Subdistrict, Village, RW


if __name__ == '__main__':

    conn = psycopg2.connect("dbname='geolevels2' user ='vagrant' password='password' ")
    cur = conn.cursor()
    sql_prov = "select * from boundary_prov;"
    print 'DEBUG prov'
    print sql_prov
    cur.execute(sql_prov)   
    rows = cur.fetchall()
    list_prov = [Province(id=row[3], name=row[2], poly=row[1]) for row in rows]
    print list_prov
    
    for prov in list_prov:
        prov.save()
        cur2 = conn.cursor()
        sql_city = "select * from boundary_kab where id_prov = %d" % prov.id
        cur2.execute(sql_city)
        rows_city = cur2.fetchall()
        list_city = [City(id=row_city[4], name=row_city[2], poly=row_city[1], province=prov) for row_city in rows_city]
        print list_city

        for city in list_city:
        	city.save()
        	cur3 = conn.cursor()
        	sql_subdistrict = "select * from boundary_kec where id_kab= %d" % city.id
        	cur3.execute(sql_subdistrict)
        	rows_subdistrict = cur3.fetchall()
        	list_subdistrict = [Subdistrict(id=row_subdistrict[5], name=row_subdistrict[2], poly=row_subdistrict[1], city=city) for row_subdistrict in rows_subdistrict]
        	print '================'
        	print city.name
        	print list_subdistrict
        	print 'DEBUG list_subdistrict'
        	print len(list_subdistrict)

        	for subdistrict in list_subdistrict:
        		subdistrict.save()
        		print subdistrict.name
        		cur4 = conn.cursor()
        		sql_village = "select * from boundary_kel where id_kec= %d" %subdistrict.id
        		cur4.execute(sql_village)
        		rows_village = cur4.fetchall()
        		list_village = [Village(id=row_village[2], name=row_village[3], poly=row_village[1], subdistrict=subdistrict) for row_village in rows_village]

        		for village in list_village:
        			village.save()
        			cur5 = conn.cursor()
        			sql_rw = "select * from boundary where id_kel= '%s'" %village.id
        			cur5.execute(sql_rw)
        			rows_rw = cur5.fetchall()
        			list_rw = [RW(id=row_rw[7], name=row_rw[5], poly=row_rw[1], area=row_rw[4], village=village) for row_rw in rows_rw]

        			for rw in list_rw:
        				print rw.id, rw.name, rw.area
        				rw.save()
