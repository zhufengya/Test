package com.itranswarp.learnjava.servlet;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(urlPatterns = "/")
public class HelloServlet extends HttpServlet {

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		resp.setContentType("text/html");
		PrintWriter pw = resp.getWriter();
		String name = req.getParameter("name");
		//http://127.0.0.1:8080/hello/?name=Bob 带参参数不能有空格！不然读取返回的name就会是那个空格了！！
		if(name != null)
			pw.write("<h1>Hello, " + name + "!</h1>");
		else
			pw.write("<h1>Hello, world!</h1>");
		pw.flush();
	}
}
