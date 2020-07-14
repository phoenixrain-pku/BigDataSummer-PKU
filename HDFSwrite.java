import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FSDataInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//本程序实现在 HDFS 中创建大批量小文件(文件内容、文件名称与文件数量皆可指定)，在全分布式Hadoop运行成功。
public class HDFSwrite {
public static void main(String[] args) throws Exception {
int i = 1;
while(i<10000) {
Configuration conf=new Configuration();
conf.set("fs.defaultFS", "hdfs://Master:9000");
conf.set("fs.hdfs.impl", "org.apache.hadoop.hdfs.DistributedFileSystem");
FileSystem fs = FileSystem.get(conf);
String fileName = i+"";
Path file = new Path(fileName);
createFile(fs,file);
readFile(fs,file);
fs.close();
++i;
}
}

public static void createFile(FileSystem fs, Path file) throws IOException{
    byte[] buff = "Hi! This is a file!".getBytes();
    FSDataOutputStream os =fs.create(file);
    os.write(buff,0,buff.length);
    System.out.println("Create:"+file.getName());
    os.close();
}
public static void readFile(FileSystem fs, Path file) throws IOException{
        FSDataInputStream in = fs.open(file);
        BufferedReader d = new BufferedReader(new InputStreamReader(in));
        String content = d.readLine();
        System.out.println(content);
        d.close();
        in.close();
}
}
