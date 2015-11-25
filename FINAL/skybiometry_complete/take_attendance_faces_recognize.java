import com.mashape.unirest.http.*;
import com.mashape.unirest.http.exceptions.*;
import java.io.*;
import org.json.*;

public class take_attendance_faces_recognize{
	public static void main(String[] args) throws UnirestException{
		String filename=args[0];
		String data_namespace=args[1];

		// These code snippets use an open-source library. http://unirest.io/java
		HttpResponse<JsonNode> response = Unirest.post("https://face.p.mashape.com/faces/recognize?api_key=10a74ff8e05245b48ef5d3fb1ca99326&api_secret=0374470e39c348c2a312fca9660b1623")
		.header("X-Mashape-Key", "BqdRVOLyQ0mshhPZZdTcyvrfPg9Cp1NtNZ5jsnPNWdTPSF4FUl")
		.field("attributes", "none")
		.field("detector", "Normal")
		.field("files", new File(filename))
		.field("limit", 64)
		.field("namespace", data_namespace)
		.field("uids", "all")
		.asJson();

		System.out.println(response.getBody());

		int n_uids = response.getBody().getObject().getJSONArray("photos").getJSONObject(0).getJSONArray("tags").getJSONObject(0).getJSONArray("uids").length();

		if(n_uids>0){
			String uid = response.getBody().getObject().getJSONArray("photos").getJSONObject(0).getJSONArray("tags").getJSONObject(0).getJSONArray("uids").getJSONObject(0).getString("uid");
			System.out.println("uid: "+ uid);
		}
		else{
			// go to a activity with text "No match! Try again!" and a button to go to the camera activity
		}

	}
}