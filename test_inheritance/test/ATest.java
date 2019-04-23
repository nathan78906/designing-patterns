import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class ATest {
  A a;

  @Before
  public void setUp(){
    this.a = new A();
  }

  @Test
  public void method1() {
    assertEquals(a.method1(), 1);
  }

  @Test
  public void method2() {
    assertEquals(a.method2(), 2);
  }
}