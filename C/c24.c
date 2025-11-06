   #include <stdio.h>
 
    main( ) {
 
        int field[4][4] = { {0,1,0,1}, {0,0,0,1}, {1,1,1,0}, {0,1,1,1} }; // (1)
        int mines[4][4] = { {0,0,0,0}, {0,0,0,0}, {0,0,0,0}, {0,0,0,0} }; // (2)
       
        int w = 4, h = 4; // (3)
        for (int y = 0; y < h; y++) { // (4)
 
            for (int x = 0; x < w; x++) { // (5)
 
                if (field[y][x] == 0) continue; // (6)
 
                for (int j = y - 1; j <= y + 1; j++) { // (7)
 
                    for (int i = x - 1; i <= x + 1; i++) { // (8)
 
                        if (chkover(w, h, j, i) == 1) //(9), (12)
 
                            mines[j][i] += 1; // (13)
                    }
                }
            }
        }
    }

    int chkover(int w, int h, int j, int i) { // (10)
 
        if (i >= 0 && i < w && j >= 0 && j < h) return 1; //(11)
 
        return 0; //(11)
 
    }