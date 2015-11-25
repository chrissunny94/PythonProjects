import com.mashape.unirest.http.*;
import com.mashape.unirest.http.exceptions.*;
import java.io.*;
import org.json.*;

public class add_students_faces_detect_save{
	static HttpResponse<JsonNode> tags_save(String api_key, String api_secret, String x_mashape_key, String tids, String uids_with_namespace) throws UnirestException, JSONException{
		// These code snippets use an open-source library. http://unirest.io/java
		HttpResponse<JsonNode> response = Unirest.post("https://face.p.mashape.com/tags/save?api_key="+api_key+"&api_secret="+api_secret)
		.header("X-Mashape-Key", x_mashape_key)
		.header("Content-Type", "application/x-www-form-urlencoded")
		.header("Accept", "application/json")
		.field("tids", tids)
		.field("uid", uids_with_namespace)
		.asJson();

		return response;
	}


	public static void main(String[] args) throws UnirestException,JSONException{		
		String filename = args[0];
		String uid_with_namespace = args[1];

		String api_key = "10a74ff8e05245b48ef5d3fb1ca99326";
		String api_secret = "0374470e39c348c2a312fca9660b1623";
		String x_mashape_key = "BqdRVOLyQ0mshhPZZdTcyvrfPg9Cp1NtNZ5jsnPNWdTPSF4FUl";

		// These code snippets use an open-source library. http://unirest.io/java
		HttpResponse<JsonNode> response = Unirest.post("https://face.p.mashape.com/faces/detect?api_key="+api_key+"&api_secret="+api_secret)
		.header("X-Mashape-Key", x_mashape_key)
		.field("attributes", "none")
		.field("detector", "Normal")
		.field("files", new File(filename))
		.asJson();

		System.out.println(response.getBody()+"\n\n");

		int n_tags = response.getBody().getObject().getJSONArray("photos").getJSONObject(0).getJSONArray("tags").length();

		if(n_tags==0){
			System.out.println("Error: No face found!");
			// go to activity with button "Click here to take picture again" which takes them to the picture taking activity
		}
		else if (n_tags>1){
			System.out.println("Error: More than one face found!");
			// go to activity with error message "Error: More than one face found!" and a button "Click here to take picture again" which takes them to the picture taking activity
		}
		else{
			String tid = response.getBody().getObject().getJSONArray("photos").getJSONObject(0).getJSONArray("tags").getJSONObject(0).getString("tid");

			// tags/save
			HttpResponse<JsonNode> tags_save_response = tags_save(api_key, api_secret, x_mashape_key, tid, uid_with_namespace);

			System.out.println(tags_save_response.getBody());
		}

	}
}