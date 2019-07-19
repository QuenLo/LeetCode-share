// ref. https://leetcode.com/problems/evaluate-division/discuss/88169/Java-AC-Solution-using-graph

package app;

import java.util.*;

class Q399_evaluate_division
{
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries)
    {
        // building the graph
        Map<String, Map<String, Double>> map = new HashMap<String, Map<String, Double>>();
        for( int i = 0; i < values.length; i++ )
        {
            String a = equations.get( i ).get( 0 );
            String b = equations.get( i ).get( 1 );
            if( !map.containsKey( a ) )
                map.put( a, new HashMap<String, Double>() );
            if( !map.containsKey( b ) )
                map.put( b, new HashMap<String, Double>() );
            map.get( a ).put( b, values[ i ] );
            map.get( b ).put( a, 1 / values[ i ] );
        }
        
        // solution set
        double[] sol = new double[ queries.size() ];
        for( int i = 0; i < queries.size(); i++ )
            sol[ i ] = dfs( queries.get( i ).get( 0 ), queries.get( i ).get( 1 ), 1, map, new HashSet<String>() );
        return sol;
    }
    
    public double dfs( String a, String b, double tmp, Map<String, Map<String, Double>> map, Set<String> visited )
    {
        // a is not in the graph or a is already visited
        // Set.add() return false if the operation failed (element exists)
        // if( !map.containsKey( a ) || !visited.add( a ) ) return -1;
        if( !map.containsKey( a ) ) return -1;
        if( visited.contains( a ) ) return -1;
        visited.add( a );

        if( a.equals( b ) ) return tmp;

        // get the edges
        Map<String, Double> edges = map.get( a );
        for( String c: edges.keySet() )
        {
            double ans = dfs( c, b, tmp * edges.get( c ), map, visited );
            if( ans != -1 ) return ans;
        }
        
        return -1;
    }
}