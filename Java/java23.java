ublic class Main {

    public static void main(String[] args) {

        B a = new D();
        D b = new D();
        System.out.print(a.getx() + a.x + b.getx() + b.x);
    }
}

class B {

    int x = 3;

    int getx() {
        return x * 2;
    }
}

class D extends B {

    int x = 7;

    int getx() {
        return x * 3;
    }
}