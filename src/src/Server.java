import org.w3c.dom.ls.LSOutput;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.sql.*;

public class Server  {
    private static final int PORT = 8080;
    private static final String DB_URL = "jdbc:mysql://localhost:3306/mydatabase";
    private static final String DB_USER = "username";
    private static final String DB_PASSWORD = "password";

    public static void main(String[] args) throws IOException{
    ServerSocket  serversocket = new ServerSocket(1234);
    Socket socket=serversocket.accept();
    System.out.println("Client connected");
        InputStreamReader input=new InputStreamReader(socket.getInputStream());
        BufferedReader bufferReader=new BufferedReader(input);

        String Text=bufferReader.readLine();
        System.out.println("Client: "+ Text);

        PrintWriter printwriter=new PrintWriter(socket.getOutputStream());
        printwriter.println("yes");
        printwriter.flush();



    }
}