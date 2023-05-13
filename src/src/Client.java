import java.io.*;
import java.net.Socket;

public class Client {
    public static void main(String[] args) throws IOException {
        Socket socket=new Socket("localhost",1234);
        PrintWriter printWriter =new PrintWriter(socket.getOutputStream());
        printWriter.println("is it working!");
        printWriter.flush();

        InputStreamReader Input=new InputStreamReader(socket.getInputStream());
        BufferedReader bufferedReader=new BufferedReader(Input);
        String Text=bufferedReader.readLine();
        System.out.println("Server:"+Text);

    }
}
