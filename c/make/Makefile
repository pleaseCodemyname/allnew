1 OBJF = test1.o test2.o test3.o
2 test : $(OBJF)
3         gcc -o $@ $^
4 test1.o : test1.c a.h
5         gcc -c $<
6 test2.o : test2.c a.h b.h
7         gcc -c $*.c
8 test3.o : test3.c b.h c.h
9         gcc -c $<
10 clean : test $(OBJF)
11         rm -rf $^
