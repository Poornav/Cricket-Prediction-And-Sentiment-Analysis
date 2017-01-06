import java.util.*;
import java.io.*;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import java.util.*;
import java.io.*;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
public class CricFinal {
	public static void main(final String[] args) throws IOException {
		//System.out.println("\nhere i am"+args[0]);
		Document doc = Jsoup.connect("http://www.cricbuzz.com/cricket-scores/2215/ind-vs-sl-final-icc-world-cup-2011").userAgent("Mozilla").timeout(20000).get();
		//Elements commentary = doc.select("div.col-sm-12.col-xs-12.col-md-8.col-lg-8.bg-white.cb-comtry-col div.row p.col-sm-11.col-md-11.col-xs-11.col-lg-11.cb-font-14.cb-comm-text");
		Elements overs = doc.select("div.col-sm-12.col-xs-12.col-md-8.col-lg-8.bg-white.cb-comtry-col div.row span.col-sm-1.col-md-1.col-xs-1.col-lg-1.cb-font-14");
		int length=overs.size();
		//System.out.println(length);
		for(int i=0;i<length;i++)
		{
			System.out.println(overs.get(i).text());
		}
		
	}
}
