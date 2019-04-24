import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class CTest extends ATest{
  C c;

  @Before
  public void setUp() {
    a = new C();
    c = new C();
  }

  @Test
  public void method1() {
    assertEquals(a.method1(), 11);
  }

  @Test
  public void method5() {
    assertEquals(c.method5(), 5);
  }
}