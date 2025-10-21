public class Main {
  static interface F {
    int apply(int x) throws Exception;
  }

  public static int run(F f) {
    try {
      return f.apply(3);
    } catch (Exception e) {
      return 7;
    }
  }

  public static void main(String[] args) {
    F f = (x) -> {
      if (x > 2)
        throw new Exception();
      return x * 2;
    };

    System.out.print(run(f) + run((int n) -> n + 9));
  }
}
