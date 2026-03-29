class Graph {

    private HashMap<Integer, HashSet<Integer>> adjList;

    public Graph() {
        adjList = new HashMap<>();
    }

    public void addEdge(int src, int dst) {
        // Put src and dst both in map
        adjList.putIfAbsent(src, new HashSet<>());
        adjList.putIfAbsent(dst, new HashSet<>());
        // Add edge if not already exists
        adjList.get(src).add(dst);
    }

    public boolean removeEdge(int src, int dst) {
        if(adjList.containsKey(src) && adjList.get(src).contains(dst)) {
            adjList.get(src).remove(dst);
            return true;
        }
        return false;
    }

    public boolean hasPath(int src, int dst) {
        if(adjList.containsKey(src) && adjList.containsKey(dst)) {
           return hasPathBFS(src, dst);
        }
        return false;
    }

    private boolean hasPathBFS(int src, int dst) {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(src);
        HashSet<Integer> visited = new HashSet<>();
        while(!q.isEmpty()) {
            int curr = q.remove();
            visited.add(curr);
            if(curr == dst)
                return true;
            for(int e : adjList.get(curr)) {
                if(!visited.contains(e)) {
                    q.add(e);
                    visited.add(e);
                }
            }
        }
        return false;
    }
}
