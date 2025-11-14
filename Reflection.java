import java.lang.reflect.*;

public class ReflectionExample {
    public static void main(String[] args) {
        try {
            // Get the Class object for a specific class
            Class<?> personClass = Class.forName("Person");
            
            // Create an instance using reflection
            Object personObj = personClass.getDeclaredConstructor().newInstance();
            
            // Get all fields
            Field[] fields = personClass.getDeclaredFields();
            System.out.println("Fields:");
            for (Field field : fields) {
                System.out.println("  " + field.getName() + " - " + field.getType());
            }
            
            // Access and modify a private field
            Field nameField = personClass.getDeclaredField("name");
            nameField.setAccessible(true); // Bypass private access
            nameField.set(personObj, "John Doe");
            
            // Get all methods
            Method[] methods = personClass.getDeclaredMethods();
            System.out.println("\nMethods:");
            for (Method method : methods) {
                System.out.println("  " + method.getName());
            }
            
            // Invoke a method using reflection
            Method getNameMethod = personClass.getMethod("getName");
            String name = (String) getNameMethod.invoke(personObj);
            System.out.println("\nName retrieved: " + name);
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// Sample Person class
class Person {
    private String name;
    private int age;
    
    public Person() {
        this.age = 0;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
}