var express = require("express");
var bodyParser = require('body-parser');
var path = require("path");
var app = express();
var nodemailer = require('nodemailer');
var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'hargun312kaur@gmail.com',
    pass: 'missgunu'
  }
});
var mysql = require("mysql");
var dbConfigObj = {
 host: "localhost",
 user: "root",
 password: "",
 database: "farmate"
};
var dbcon = mysql.createConnection(dbConfigObj);
dbcon.connect(function (err) {
 if (err) {
  console.log(err.message);
 }
 else {
  console.log("Connected Successfully");
 }
});
app.use(express.static("public"));
app.post(express.urlencoded({extended:true}));
const port=process.env.PORT||2007;
app.listen(port, function () {
  console.log(port);
 console.log("Server Started");
});
// const http = require('http');
// const hostname='0.0.0.0';
// app.listen(port,hostname,()=>{
//   console.log(`Server running at http://${hostname}:${port}/`);
// })
app.get("/home", function (req, resp) {
 resp.sendFile(process.cwd() + "/public/index.html");
});
app.get("/ajax-check-user", function (req, resp) {
 //console.log(req.query.email);
 dbcon.query("select * from userss where email=?", [req.query.email], function (err, res) {
  //console.log(res);
  resp.send(res);
 });
});
app.get("/ajax-signup-user", function (req, resp) {
  console.log(req.query);
 var data = [req.query.email, req.query.password, req.query.mobile, req.query.name, req.query.dos];
 console.log(data);
 dbcon.query("insert into userss values(?,?,?,?,current_date)", data, function (err) {
  if (err) {
   console.log(err.message);
  }
  else {
   console.log("Data uploaded");
  }
 });
});
app.get("/ajax-login-user", function (req, resp) {
 //console.log(req.query);
 dbcon.query("select email from userss where (email=? and password=?)", [req.query.email, req.query.password], function (err, res) {
  console.log(res);
  resp.send(res);
 });
});
app.get("/forgot",function(req,resp){
 dbcon.query("select * from userss where email=?",[req.query.email],function(err,res){
  console.log(res);
  var mailOptions = {
  from: 'hargun312kaur@gmail.com',
  to: req.query.email,
  subject: 'Password for Farmate',
  html: '<h4>Your password for the Farmate account is "'+res[0].password+'".</h4><br><p>Please click on the following link to <a href="index.html">Login</a>. </p>'
  };
  transporter.sendMail(mailOptions, function(error, info){
    if (error) {
      console.log(error);
    } else {
      console.log('Email sent: ' + info.response);
    }
  });
  resp.send(res);
 });
});

var fileuploading= require("express-fileupload");
app.use(fileuploading());
app.post(express.urlencoded({extended:true}));

app.post("/change-name",function(req,resp){
  // console.log("hi");
  // console.log(req.files);
 var data = [req.body.name, req.body.email,req.body.contact];
 dbcon.query("update userss set name=?,mobile=? where email=?",data,function(err){
  if(err){
   console.log(err.message);
  }
  else{
   console.log("Name Updated");
   resp.redirect("profile.html");
  }
 });
 
});
app.post("/profile", function (req, resp) {
 if(req.files==null){
  req.body.picname="nopic";
 }
 else{
  req.body.picname=req.files.ppic.name;
  console.log(req.body);
  console.log(process.cwd());
  var uploadingPath=process.cwd()+"/public"+"/uploads/"+req.files.ppic.name;
  req.files.ppic.mv(uploadingPath,function(err){
  if(err){
   console.log(err);
  }
  else{
   console.log("Object uploaded");
  }
 });
 req.body.picname=req.files.ppic.name;
 var data = [req.body.email, req.body.name, req.body.contact, req.body.address, req.body.acard, req.body.picname];
 dbcon.query("insert into profiless values(?,?,?,?,?,?)", data, function (err) {
  if (err) {
   console.log("*    "+err.message);
  }
  else {
   console.log("Data uploaded");
   resp.redirect("profile.html");
  }
 });
 }
});
app.post("/update-profile",function(req,resp){
  // console.log("hi");
  // console.log(req.files);
 if(req.files==null){
  req.body.picname=req.body.picture;
 }
 else{
  req.body.picname=req.files.ppic.name;
  console.log(req.body);
  console.log(process.cwd());
  var uploadingPath=process.cwd()+"/public"+"/uploads/"+req.files.ppic.name;
  req.files.ppic.mv(uploadingPath,function(err){
  if(err){
   console.log(err);
  }
  else{
   console.log("Object uploaded");
  }
 });
 req.body.picname=req.files.ppic.name;}
 var data = [req.body.name, req.body.contact, req.body.address, req.body.acard, req.body.picname, req.body.email];
 dbcon.query("update profiless set name=?,	contact=?,	address=?, acard=?, picname=? where email=?",data,function(err){
  if(err){
   console.log(err.message);
  }
  else{
   console.log("Updated");
   resp.redirect("profile.html");
  }
 });
});
app.post("/check-user",function(req,resp){
  //console.log(req.query.email);
  dbcon.query("select * from profiless where email=?",[req.query.email],function(err,res){
    //console.log(res);
    resp.send(res);
  });
});
app.post("/land-save", function (req, resp) {
  // req.body.picname=req.files.pic.name;
  console.log(req.body);
//   console.log(process.cwd());
//   var uploadingPath=process.cwd()+"/public"+"/uploads/"+req.files.pic.name;
//   req.files.pic.mv(uploadingPath,function(err){
//   if(err){
//    console.log(err);
//   }
//   else{
//    console.log("Object uploaded");
//   }
//  });
 var data = [req.body.email, req.body.loc, req.body.landname, req.body.area, req.body.n, req.body.p, req.body.k, req.body.ph, req.body.moisture, req.body.type, req.body.doa, req.body.status];
 dbcon.query("insert into landd values(null,?,?,?,?,?,?,?,?,?,?,current_date,1)", data, function (err) {
  if (err) {
   console.log("*    "+err.message);
  }
  else {
   console.log("Data uploaded");
   resp.redirect("newland.html");
  }
 });
});
// app.get("/getrid",function(req,resp){
//   //console.log(req.query.rid);
//   dbcon.query("select rid from mediciness where landname=?",[req.query.landname],function(err,res){
//     //console.log(res);
//     resp.send(res);
//   });
// });
app.get("/getinf",function(req,resp){
  //console.log(req.query.rid);
  dbcon.query("select * from landd where rid=?",[req.query.rid],function(err,res){
    //console.log(res);
    resp.send(res);
  });
});
app.post("/land-update",function(req,resp){
//   req.body.picname=req.files.pic.name;
//   var uploadingPath=process.cwd()+"/public"+"/uploads/"+req.files.pic.name;
//   req.files.pic.mv(uploadingPath,function(err){
//   if(err){
//    console.log(err);
//   }
//   else{
//    console.log("Object uploaded");
//   }
//  });
  var data = [req.body.loc, req.body.landname, req.body.area, req.body.n, req.body.p, req.body.k, req.body.ph, req.body.moisture, req.body.type, req.body.rid];
 dbcon.query("update landd set loc=?,	landname=?, area=?,	n=?,	p=?, k=?, ph=?, moisture=?, type=? where rid=?",data,function(err){
  if(err){
   console.log(err.message);
  }
  else{
    console.log
   console.log("Updated");
   resp.redirect("newland.html");
  }
 });
});
app.get("/fetchland",function(req,resp){
 dbcon.query("select * from landd where status=1 and email=?",[req.query.email],function(err,res){
  resp.send(res);
 });
});
app.get("/delland",function(req,resp){
 //console.log(req.query.rid);
 dbcon.query("update landd set status=0 where rid=?",[req.query.rid],function(err,res){
  if(err){
   console.log(err.message);
  }
  else{
   resp.send();
  }
 });
});
app.get("/undoland",function(req,resp){
 //console.log(req.query.rid);
 dbcon.query("update landd set status=1 where status=0 and rid=?",[req.query.rid],function(err,res){
  if(err){
   console.log(err.message);
  }
  else{
   resp.send();
  }
 });
});
app.post("/crop-rec",recommendCrop);
function recommendCrop(req,res)
{
  // console.log(req.query);
  var spawn = require("child_process").spawn;
    var process = spawn('python',["./croprecmain.py",
                            req.query.n,req.query.p,req.query.k,req.query.temp,req.query.hum,req.query.ph,req.query.rainfall] );
    // var process = spawn('python',["./croprecmain.py",
    //                         req.body.n,req.body.p,req.body.k,req.body.temperature,req.body.humidity,req.body.ph,req.body.rainfall] );
    process.stdout.on('data', function(data) {
        res.send(data.toString());
        // console.log(data.toString());
    } )
}
app.post("/fert-rec",recommendFert);
function recommendFert(req,res)
{
  // console.log(req.query);
  var spawn = require("child_process").spawn;
    var process = spawn('python',["./fertreccmain.py",
                            req.query.temp,req.query.hum,req.query.mois,req.query.type,req.query.ctype,req.query.n,req.query.k,req.query.p] );
    // var process = spawn('python',["./croprecmain.py",
    //                         req.body.n,req.body.p,req.body.k,req.body.temperature,req.body.humidity,req.body.ph,req.body.rainfall] );
    process.stdout.on('data', function(data) {
        res.send(data.toString());
        // console.log(data.toString());
    } )
}
app.post("/yield-pre",predictYield);
function predictYield(req,res)
{
  // console.log(req.query);
  var spawn = require("child_process").spawn;
    var process = spawn('python',["./yieldmain.py",
                            req.query.season,req.query.crop,req.query.area] );
    // var process = spawn('python',["./croprecmain.py",
    //                         req.body.n,req.body.p,req.body.k,req.body.temperature,req.body.humidity,req.body.ph,req.body.rainfall] );
    process.stdout.on('data', function(data) {
        res.send(data.toString());
        // console.log(data.toString());
    } )
}

// app.use(express.json());
// app.use(express.urlencoded({ extended: true }));
// const multer = require("multer");
// const upload = multer({ dest: "public/uploads/" });
// app.post("/disease",upload.array("file"), detectDisease);
// app.post("/disease", detectDisease);
// function detectDisease(req, res) {
//   // console.log(req.body);
//   // console.log(req.files);
//   // res.json({ message: "Successfully uploaded files" });
//   // console.log(req.query);
//   // console.log(req.body);
//   // console.log(process.cwd());
//   var uploadingPath="C:/Users/hargu/Farmate"+"/public"+"/uploads/"+"infect.jpg";
//   req.files.pic.mv(uploadingPath,function(err){
//   if(err){
//    console.log(err);
//   }
//   else{
//   //  console.log("Object uploaded");
//   }
//  });
//   var spawn = require("child_process").spawn;
//     var process = spawn('python',["./vib.py",uploadingPath] );
//     process.stdout.on('data', function(data) {
//     var d=data.toString();
//     // console.log(d);
//       console.log(data.toString());
//     // res.json(d);
//     } )
// }