package java.com.leetcode;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

class SubdomainVisitCount {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String,Integer> counts = new HashMap<>();
        List<String> answer = new LinkedList<>();

        for( String domain : cpdomains ){
            int hits =  Integer.parseInt(domain.substring(0,domain.indexOf(" ")));
            String curr = domain.substring(domain.indexOf(" ")+1);
            while (!curr.isEmpty()){
                counts.put(curr, counts.getOrDefault(curr, 0) + hits);
                int idx = curr.indexOf(".");
                if (idx != -1){
                    curr = curr.substring(idx+1);
                }else{
                    curr = "";
                }
            }
        }

        for (String key : counts.keySet()){
            int count =  counts.get(key);
            answer.add(count+ " " +key);
        }
        return answer;
    }
}