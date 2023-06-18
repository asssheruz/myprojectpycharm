package Homework_4;

public class Homework_4 {
    public static void main(String[] args) {
        Homework_4 primer = new Homework_4();
        for (int i = 0; i < 41; i++) {
            primer.put( i, i + 1);
        }

        System.out.println(primer.get(25));
        System.out.println(primer.remove(25));
        System.out.println(primer.get(25));
        System.out.println(primer.get(5));
        System.out.println(primer.replays(5, 10));
        System.out.println(primer.get(5));
        System.out.println(primer.size());
        System.out.println(primer.containsKey(15));
        System.out.println(primer.containsKey(60));
        System.out.println(primer.containsValue(10));
        System.out.println(primer.containsValue(100));
    }

    Node head;
    Node[] massiv = new Node[16];

    //boolean containsValue(Integer v) проверка наличия ключа значения
    public boolean containsValue(Integer v){
        int len_massiv = massiv.length;
        for (int index = 0; index < len_massiv; index++) {
            if (massiv[index] != null) {
                Node tempNode = massiv[index];
            while (tempNode != null) {
                if (tempNode.value == v) {
                    return true;
                }
                tempNode = tempNode.next;
                }
            }
        }
        return false;
    }

    //boolean containsKey(Integer key) проверка наличия ключа
    public boolean containsKey(Integer key){
        int index = key.hashCode()%16;
        if (massiv[index] != null) {
            Node tempNode = massiv[index];
            while (tempNode != null) {
                if (tempNode.key == key) {
                    return true;
                }
                tempNode = tempNode.next;
            }
        }
        return false;
    }

    //int size() количество элементов
    public Integer size(){
        int len_massiv = massiv.length;
        int result = 0;
        for (int index = 0; index < len_massiv; index++) {
            if (massiv[index] != null) {
                Node tempNode = massiv[index];
            while (tempNode != null) {
                result = result + 1;
                tempNode = tempNode.next;
                }
            }
        }
            return result;
        }


    //Object replays(Integer key, Integer v) заменить значение
    public Object replays(Integer key, Integer v) {
        int index = key.hashCode()%16;
        if (massiv[index] != null) {
            Node tempNode = massiv[index];
            while (tempNode != null) {
                if (tempNode.key == key) {
                    Integer x = tempNode.value;
                    tempNode.value = v;
                    return x;
                }
                tempNode = tempNode.next;
            }
        }
        return null;
    }


    //Object remove(Integer key) удалить элемент с соответствующем ключём
    public Object remove(Integer key) {
        int index = key.hashCode()%16;
        if (massiv[index] != null) {
            Node tempNode = massiv[index];
            if (tempNode.key == key && tempNode.next == null) {
                massiv[index] = null;
                return tempNode.value;
            }
            if (tempNode.key == key && tempNode.next != null) {
                massiv[index] = tempNode.next;
                return tempNode.value;
            }
            while (tempNode.next != null){
                if (tempNode.next.key == key){
                    Integer tmp = tempNode.next.value;
                    tempNode.next = tempNode.next.next;
                    return tmp;
                }
                tempNode = tempNode.next;
            }
        }
        return null;
    }


    //Object get(Integer key) получить значение соответствующее ключу
    public Object get(Integer key) {
        int index = key.hashCode()%16;
        if (massiv[index] != null) {
            Node tempNode = massiv[index];
            while (tempNode != null) {
                if (tempNode.key == key) {
                    return tempNode.value;
                }
                tempNode = tempNode.next;
            }
        }
        return null;
    }


    //Object put(Integer key , Integer value) добавить элемент
    public Object put(Integer key , Integer value) {
        Node temp = new Node();
        temp.value = value;
        temp.key = key;
        temp.hash = temp.key.hashCode() % 16;
        if (massiv[temp.hash] != null) {
            Node tempNode = massiv[temp.hash];
            while (tempNode != null) {
                if (tempNode.key == key) {
                    return tempNode.value;
                }
                tempNode = tempNode.next;
            }
            temp.next = massiv[temp.hash];
        }
        massiv[temp.hash] = temp;
        return null;
    }
}

# Реализовать класс работающий по принципу HashMap.
# Включая внутренний массив узлов с индексацией по
# хешу и описание узла.
class Node {
    Integer key, value;
    int hash;
    Node next;
}

