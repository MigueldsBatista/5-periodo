package REQUISITOS.design_patterns.singleton;

public class Program {
    public static void main(String[] args) {
        Singleton singleton = Singleton.getInstance();
        Singleton singleton2 = Singleton.getInstance();
        var isEqual = singleton.equals(singleton2);
       System.out.println(isEqual);;
    }
}
