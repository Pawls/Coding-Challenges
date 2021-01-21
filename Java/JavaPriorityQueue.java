import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.*;

class StudentComparator implements Comparator<Student> {
    public int compare(Student a, Student b) {
        if (a.getCGPA() < b.getCGPA()){
            return 1;
        } else if (a.getCGPA() > b.getCGPA()) {
            return -1;
        } else {
            int order = a.getName().compareTo(b.getName());
            if (order < 0) {
                return -1;
            } else if (order > 0) {
                return 1;
            } else if (a.getID() < b.getID()) {
                return -1;
            } 
        }
        return 1;
    }
}

class Student {
    private int id;
    private String name;
    private double cgpa;
    
    public Student (int id, String name, double cgpa) {
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }
    
    public String getName() {
        return this.name;
    }
    
    public int getID() {
        return this.id;
    }
    
    public double getCGPA() {
        return this.cgpa;
    }
}

class Priorities {
    public List<Student> getStudents(List<String> events) {
        PriorityQueue<Student> students = new PriorityQueue<Student>(10, new StudentComparator());
        
        for (String s : events) {
            String[] words = s.split(" ");
            if (words[0].equals("SERVED")){
                students.poll();
            } else {
                students.add(new Student(Integer.parseInt(words[3]), words[1], Float.parseFloat(words[2])));
            }
        }

        List<Student> result = new ArrayList<Student>();
        while (!students.isEmpty()){
          result.add(students.poll());
        }
        return result;
    }
}

public class Solution {
    private final static Scanner scan = new Scanner(System.in);
    private final static Priorities priorities = new Priorities();
    
    public static void main(String[] args) {
        int totalEvents = Integer.parseInt(scan.nextLine());    
        List<String> events = new ArrayList<>();
        
        while (totalEvents-- != 0) {
            String event = scan.nextLine();
            events.add(event);
        }
        
        List<Student> students = priorities.getStudents(events);
        
        if (students.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Student st: students) {
                System.out.println(st.getName());
            }
        }
    }
}