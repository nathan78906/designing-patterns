import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class BTest extends ATest {
  B b;

  @Before
  public void setUp() {
    a = new B();
    b = new B();
  }

  @Test
  public void method1() {
    assertEquals(a.method1(), 1);
  }

  @Test
  public void method2() {
    assertEquals(a.method2(), 2);
  }

  @Test
  public void method3() {
    assertEquals(b.method3(), 3);
  }

  @Test
  public void method4() {
    assertEquals(b.method4(), 4);
  }
}