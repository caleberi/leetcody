package java_leetcode.com.leetcode;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class PhoneNumberParser {

    static HashMap<String,String>  prefixToServiceProvider =  new HashMap<>();

    static {
        
        String[] mtn =  {"0703","0706","0803","0806","0810","0813","0814","0816","0903","0906","0913","0916","07025","07026","0704"};
        for (String p : mtn){
            prefixToServiceProvider.put(p, "<MTN>");
        }

        String[] airtel = {"0701","0708","0802","0808","0812","0901","0902","0904","0907","0912"};
        for (String p : airtel){
            prefixToServiceProvider.put(p, "<AIRTEL>");
        }

        String[] globalcom = {"0705","0805","0807","0811","0815","0905","0915"};
        for (String p : globalcom){
            prefixToServiceProvider.put(p, "<GLOBALCOM>");
        }

        String[] mobile9 = {"0809","0817","0818","0909","0908"};
        for (String p : mobile9){
            prefixToServiceProvider.put(p, "<9MOBILE>");
        }
        prefixToServiceProvider.put("0804", "<MTEL>");    

    }

    public static List<String> getFileData(String fileName) throws FileNotFoundException {
        try {
          File file = new File(fileName);
          Scanner reader = new Scanner(file);
          List<String> ret =  new  LinkedList<>();
          while (reader.hasNextLine()) {
            ret.add(reader.nextLine());
          }
          reader.close();
          return ret;
        } catch (FileNotFoundException err) {
            throw err;
        }
    }

    public static void main(String[] args) throws FileNotFoundException {
        List<String> phoneNumbers = getFileData("/Users/kudiadmin/Desktop/personal/LeetCode/java_leetcode/PhoneNumbers.txt");
        HashMap<String,Integer> count =  new HashMap<>();
        for (String phone : phoneNumbers) {
            String prefix4 =  phone.substring(0, 4);
            if (prefixToServiceProvider.containsKey(prefix4)){
                if(!count.containsKey(prefixToServiceProvider.get(prefix4))){
                    count.put(prefixToServiceProvider.get(prefix4), 0);
                }else{
                    count.put(prefixToServiceProvider.get(prefix4), count.get(prefixToServiceProvider.get(prefix4))+1);
                }
            } else {
                String prefix5 =  phone.substring(0, 5);
                if (prefixToServiceProvider.containsKey(prefix5)){
                    if(!count.containsKey(prefixToServiceProvider.get(prefix5))){
                        count.putIfAbsent(prefixToServiceProvider.get(prefix5), 0);
                    }else{
                        count.put(prefixToServiceProvider.get(prefix4), count.get(prefixToServiceProvider.get(prefix5))+1);
                    }
                }
            }
        }
        for (Map.Entry<String,Integer> entry : count.entrySet()){
            System.out.println(entry.getKey()+" :-> "+ entry.getValue());
        }
    }
}
