package com.company.ooo;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
class ooo {
    public static void main(String[] args)
    {
        Adnan r=new Adnan();
    }
}

class Adnan extends JFrame implements ActionListener {

    JFrame f1, f2, f3,f4,f5,f6,f7;
    JLabel f1h,clk,clk1,f2h ,f3h,imgfr3,imgfr5,name , age , gender , mobile ,email ,department , section , bloodgroup, sporttype,sport,playmode,chooseteampref,chooseclan,regmsg,img,img0,img1,img2,img3,thank;
    JTextField namet,aget,mobilet,emailt;
    JRadioButton male , female;
    JComboBox dept,sec,blood , sptype ,sp ,playmodej,ctp1,ctp2,ctp3,cc,sptype1,sp1 ,playmodej1,ctp11,ctp21,ctp31;
    JButton click , submit , cinfreg ,exit,cinfreg12,exit1,finish;
    JTextArea ta,ta1;
    String d[] = {  "CSE", "ECE", "EEE", "ME", "BBA", "AIDS"};
    String s[] = { "SECTION-A", "SECTION-B", "SECTION-C", "SECTION-D"};
    String b[] = {"A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"};
    String a[] = { "INDOOR", " OUTDOOR "};
    String a1[]= {"CRICKET","VOLLEYBALL","TABLE-TENNIS","TENNIS","BASEBALL","BASKET-BALL","BADMINTON","HOCKEY"};
    String a2[]= {"SINGLES","DOUBLES","TEAM"};
    String a3[]= {"TEAM-A","TEAM-B","TEAM-C","TEAM-D","TEAM-E"};
    String a4[]= {"HUSSY","KAPIL","YOGI","MODI","NATHURAM","DAVUD-IBRAHEEM","VIJAY-MALIYA"};
    String a5[] = { "INDOOR"};
    String a6[]= {"TABLE-TENNIS","CHESS","CARROM"};



    Adnan(){
        f1 = new JFrame();
        f2 = new JFrame();
        f3 = new JFrame();
        f4 = new JFrame();
        f5 = new JFrame();
        f6 = new JFrame();
        f7 = new JFrame();

        f1h = new JLabel("REGISTRATIONS FOR SPORTS");
        f1h.setFont(new java.awt.Font("Tahoma", 1, 24)); // NOI18N
        f1h.setForeground(new java.awt.Color(102, 0, 255));
        f1h.setBounds(180, 20, 410, 70);

        click = new JButton("HERE");
        click.setBackground(new java.awt.Color(204, 255, 255));
        click.setFont(new java.awt.Font("Tahoma", 1, 18)); // NOI18N
        click.setBounds(310, 280, 100, 40);

        img1=new JLabel();
        img1.setIcon(new javax.swing.ImageIcon("C:\\Users\\Mohammed Adnan\\OneDrive\\Desktop\\sp5.jpg")); // NOI18N
        img1.setMaximumSize(new java.awt.Dimension(600, 600));
        img1.setMinimumSize(new java.awt.Dimension(600, 600));
        img1.setBounds(0, 0, 698, 475);

        clk = new JLabel("Click");
        clk.setFont(new java.awt.Font("Tahoma", 1, 18)); // NOI18N
        clk.setBounds(250, 280, 50, 40);

        clk1 = new JLabel("To Register");
        clk1.setFont(new java.awt.Font("Tahoma", 1, 18)); // NOI18N
        clk1.setBounds(420, 280, 150, 40);

        f1.add(f1h);
        f1.add(click);
        f1.add(clk);
        f1.add(clk1);
        f1.add(img1);

        f2h = new JLabel("ENTER DETAILS");
        f2h.setFont(new java.awt.Font("Tahoma", 1, 18)); // NOI18N
        f2h.setBounds(230, 20, 160, 30);

        name = new JLabel("NAME");
        name.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        name.setBounds(20, 60, 80, 20);

        namet = new JTextField();
        namet.setBounds(120, 50, 120, 30);

        age = new JLabel("AGE");
        age.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        age.setBounds(20, 90, 60, 20);

        aget = new JTextField();
        aget.setBounds(120, 90, 120, 30);

        gender = new JLabel("GENDER");
        gender.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        gender.setBounds(20, 130, 60, 20);

        male = new JRadioButton("MALE");
        male.setBounds(120, 130, 60, 20);

        female = new JRadioButton("FEMALE");
        female.setBounds(190, 130, 70, 20);

        mobile = new JLabel("MOBILE");
        mobile.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        mobile.setBounds(20, 170, 60, 20);

        mobilet = new JTextField();
        mobilet.setBounds(120, 160, 120, 30);

        email = new JLabel("E-MAIL");
        email.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        email.setBounds(20, 210, 70, 20);

        emailt = new JTextField();
        emailt.setBounds(120, 210, 180, 30);

        department = new JLabel("DEPARTMENT");
        department.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        department.setBounds(20, 260, 90, 20);

        dept = new JComboBox(d);
        dept.setBounds(120, 250, 110, 30);

        section = new JLabel("SECTION");
        section.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        section.setBounds(20, 310, 80, 20);

        sec = new JComboBox(s);
        sec.setBounds(120, 300, 110, 30);

        bloodgroup = new JLabel("BLOOD GROUP");
        bloodgroup.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        bloodgroup.setBounds(280, 170, 100, 20);

        blood = new JComboBox(b);
        blood.setBounds(400, 170, 48, 20);

        submit = new JButton("SUBMIT");
        submit.setFont(new java.awt.Font("Tahoma", 1, 18)); // NOI18N
        submit.setBounds(240, 370, 140, 30);

        img0 = new JLabel();
        img0.setIcon(new javax.swing.ImageIcon("C:\\Users\\Mohammed Adnan\\OneDrive\\Desktop\\SP7.jpg")); // NOI18N
        img0.setBounds(4, 4, 610, 480);

        f2.add(name);
        f2.add(age);
        f2.add(gender);
        f2.add(email);
        f2.add(mobile);
        f2.add(department);
        f2.add(section);
        f2.add(bloodgroup);
        f2.add(namet);
        f2.add(aget);
        f2.add(emailt);
        f2.add(mobilet);
        f2.add(dept);
        f2.add(sec);
        f2.add(blood);
        f2.add(male);
        f2.add(female);
        f2.add(f2h);
        f2.add(submit);
        f2.add(img0);

        f3h = new JLabel("MAKE SELECTION");
        f3h.setFont(new java.awt.Font("Tahoma", 1, 18)); // NOI18N
        f3h.setBounds(230, 20, 200, 30);

        sporttype = new JLabel("SPORT TYPE");
        sporttype.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        sporttype.setBounds(20, 60, 80, 20);

        sptype = new JComboBox(a);
        sptype.setBounds(120, 50, 120, 30);

        sport = new JLabel("SPORT");
        sport.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        sport.setBounds(20, 90, 60, 20);

        sp = new JComboBox(a1);
        sp.setBounds(120, 90, 120, 30);

        playmode = new JLabel("PLAY MODE ");
        playmode.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        playmode.setBounds(20, 130, 90, 20);

        playmodej = new JComboBox(a2);
        playmodej.setBounds(120, 130, 120, 20);

        chooseteampref = new JLabel("CHOOSE TEAM PREFERANCES ");
        chooseteampref.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        chooseteampref.setBounds(20, 170, 200, 20);

        ctp1 = new JComboBox(a3);
        ctp1.setBounds(250, 170, 80, 20);
        ctp2 = new JComboBox(a3);
        ctp2.setBounds(340, 170, 80, 20);
        ctp3 = new JComboBox(a3);
        ctp3.setBounds(430, 170, 80, 20);

        chooseclan = new JLabel("CHOOSE CLAN");
        chooseclan.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        chooseclan.setBounds(20, 210, 100, 20);

        cc = new JComboBox(a4);
        cc.setBounds(250, 210, 180, 30);

        cinfreg = new JButton("CINFIRM REGISTRATION");
        cinfreg.setFont(new java.awt.Font("Tahoma", 1, 18)); // NOI18N
        cinfreg.setBounds(50, 260 , 350,40);

        imgfr3 = new JLabel();
        imgfr3.setIcon(new javax.swing.ImageIcon("C:\\Users\\Mohammed Adnan\\OneDrive\\Desktop\\s23.jfif")); // NOI18N
        imgfr3.setBounds(0, 0, 590, 450);


        f3.add(sporttype);
        f3.add(sport);
        f3.add(playmode);
        f3.add(chooseteampref);
        f3.add(chooseclan);
        f3.add(cinfreg);
        f3.add(sptype);
        f3.add(sp);
        f3.add(playmodej);
        f3.add(ctp1);
        f3.add(ctp2);
        f3.add(ctp3);
        f3.add(cc);
        f3.add(f3h);
        f3.add(imgfr3);

        click.addActionListener(this);
        submit.addActionListener(this);
        cinfreg.addActionListener(this);

        f1.setLayout(null);
        f1.setSize(800,800);
        f1.setVisible(true);
        f2.setLayout(null);
        f2.setSize(800, 800);
        f3.setLayout(null);
        f3.setSize(650, 600);

        f1.getContentPane().setBackground(Color.PINK);
        f2.getContentPane().setBackground(Color.PINK);
        f3.getContentPane().setBackground(Color.PINK);

        regmsg = new JLabel("Registered Successfully!!!");
        regmsg.setFont(new java.awt.Font("Tahoma", 2, 18)); // NOI18N
        regmsg.setBounds(200, 40, 250, 50);

        ta = new JTextArea();
        ta.setBounds(100, 100, 400, 200);

        exit = new JButton("MAKE ANOTHER REGISTRATION");
        exit.setBounds(100, 320 , 270,40);
        exit.addActionListener(this);

        exit1 = new JButton("FINISH");
        exit1.setBounds(400, 320 , 100,40);
        exit1.addActionListener(this);

        img = new JLabel();
        img.setIcon(new javax.swing.ImageIcon("C:\\Users\\Mohammed Adnan\\OneDrive\\Desktop\\sp11.jpg")); // NOI18N
        img.setBounds(0, -250, 640, 710);


        f4.setLayout(null);
        f4.setSize(800, 800);

        f4.add(regmsg);
        f4.add(exit);
        f4.add(exit1);
        f4.add(ta);
        f4.add(img);

        JLabel f4h = new JLabel("MAKE SELECTION");
        f4h.setFont(new java.awt.Font("Tahoma", 1, 18)); // NOI18N
        f4h.setBounds(230, 20, 200, 30);

        JLabel sporttype1 = new JLabel("SPORT TYPE");
        sporttype1.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        sporttype1.setBounds(20, 60, 80, 20);

        sptype1 = new JComboBox(a5);
        sptype1.setBounds(120, 50, 120, 30);

        JLabel sport1 = new JLabel("SPORT");
        sport1.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        sport1.setBounds(20, 90, 60, 20);

        sp1 = new JComboBox(a6);
        sp1.setBounds(120, 90, 120, 30);

        JLabel playmode1 = new JLabel("PLAY MODE ");
        playmode1.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        playmode1.setBounds(20, 130, 90, 20);

        playmodej1 = new JComboBox(a2);
        playmodej1.setBounds(120, 130, 120, 20);

        JLabel chooseteampref1 = new JLabel("CHOOSE TEAM PREFERANCES ");
        chooseteampref1.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        chooseteampref1.setBounds(20, 170, 200, 20);

        ctp11 = new JComboBox(a3);
        ctp11.setBounds(250, 170, 80, 20);
        ctp21 = new JComboBox(a3);
        ctp21.setBounds(340, 170, 80, 20);
        ctp31 = new JComboBox(a3);
        ctp31.setBounds(430, 170, 80, 20);


        cinfreg12 = new JButton("CINFIRM REGISTRATION(S)");
        cinfreg12.setFont(new java.awt.Font("Tahoma", 1, 18)); // NOI18N
        cinfreg12.setBounds(50, 260 , 350,40);
        cinfreg12.addActionListener(this);

        imgfr5 = new JLabel();
        imgfr5.setIcon(new javax.swing.ImageIcon("C:\\Users\\Mohammed Adnan\\OneDrive\\Desktop\\s24.jfif")); // NOI18N
        imgfr5.setBounds(0, 0, 630, 450);

        f5.setLayout(null);
        f5.setSize(800, 800);

        f5.add(sporttype1);
        f5.add(sport1);
        f5.add(playmode1);
        f5.add(chooseteampref1);
        f5.add(cinfreg12);
        f5.add(sptype1);
        f5.add(sp1);
        f5.add(playmodej1);
        f5.add(ctp11);
        f5.add(ctp21);
        f5.add(ctp31);
        f5.add(f4h);
        f5.add(imgfr5);

        JLabel fr6l1 = new JLabel("Registered Successfully!!!");
        fr6l1.setFont(new java.awt.Font("Tahoma", 2, 18)); // NOI18N
        fr6l1.setBounds(200, 40, 250, 50);

        ta1 = new JTextArea();
        ta1.setBounds(100, 100, 400, 200);

        finish = new JButton("FINISH");
        finish.setBounds(250, 360 , 120,40);
        finish.addActionListener(this);

        img2 = new JLabel();
        img2.setIcon(new javax.swing.ImageIcon("C:\\Users\\Mohammed Adnan\\OneDrive\\Desktop\\s26.jpg")); // NOI18N
        img2.setBounds(0, 0, 680, 520);

        f6.setLayout(null);
        f6.setSize(800, 800);

        f6.add(fr6l1);
        f6.add(ta1);
        f6.add(finish);
        f6.add(img2);

        thank = new JLabel("THANK YOU");
        thank.setFont(new java.awt.Font("Wide Latin", 3, 24)); // NOI18N
        thank.setForeground(new java.awt.Color(255, 255, 255));
        thank.setBounds(180, 360, 300, 30);

        img3 = new JLabel();
        img3.setIcon(new javax.swing.ImageIcon("C:\\Users\\Mohammed Adnan\\OneDrive\\Desktop\\s21.jpg")); // NOI18N
        img3.setBounds(0, 40, 690, 414);

        f7.setLayout(null);
        f7.setSize(700, 485);


        f7.add(thank);
        f7.add(img3);


    }

    @Override
    public void actionPerformed(ActionEvent ae) {

        String Name = namet.getText();
        String Age = aget.getText();
        String Mobile = mobilet.getText();
        String Email = emailt.getText();
        dept.getSelectedItem();
        sec.getSelectedItem();
        blood.getSelectedItem();
        sptype.getSelectedItem();
        sp.getSelectedItem();
        playmodej.getSelectedItem();
        ctp1.getSelectedItem();
        ctp2.getSelectedItem();
        ctp3.getSelectedItem();
        cc.getSelectedItem();
        sp1.getSelectedItem();
        sptype1.getSelectedItem();
        playmodej1.getSelectedItem();
        ctp21.getSelectedItem();
        ctp11.getSelectedItem();
        ctp31.getSelectedItem();

        String text =
                "NAME       :"+Name+"\n"+
                        "AGE        :"+Age+"\n"+
                        "GENDER     : MALE"+"\n"+
                        "MOBILE     :"+Mobile+"\n"+
                        "E-MAIL     :"+Email+"\n"+
                        "DEPARTMENT :"+dept.getSelectedItem()+"\n"+
                        "SECTION    :"+sec.getSelectedItem()+"\n"+
                        "BLOOD GROUP:"+blood.getSelectedItem()+"\n"+
                        "SPORT      :"+sp.getSelectedItem()+"\n"+
                        "PLAY MODE  :"+playmodej.getSelectedItem()+"\n"+
                        "CLAN       :"+cc.getSelectedItem();

        ta.setText(text);

        String text1 =
                "NAME       :"+Name+"\n"+
                        "AGE        :"+Age+"\n"+
                        "GENDER     : MALE"+"\n"+
                        "MOBILE     :"+Mobile+"\n"+
                        "E-MAIL     :"+Email+"\n"+
                        "DEPARTMENT :"+dept.getSelectedItem()+"\n"+
                        "SECTION    :"+sec.getSelectedItem()+"\n"+
                        "BLOOD GROUP:"+blood.getSelectedItem()+"\n"+
                        "SPORT      :"+sp1.getSelectedItem()+"\n"+
                        "PLAY MODE  :"+playmodej1.getSelectedItem()+"\n"+
                        "CLAN       :"+cc.getSelectedItem();
        ta1.setText(text1);

        if (ae.getSource() == click)
        {
            f1.dispose();
            f2.setVisible(true);
        }

        else if (ae.getSource() == submit)
        {

            f2.dispose();
            f3.setVisible(true);

        }
        else if (ae.getSource() == cinfreg) {

            f3.dispose();
            f4.setVisible(true);
        }
        else if (ae.getSource() == exit) {

            f4.dispose();
            f5.setVisible(true);
        }
        else if (ae.getSource() == cinfreg12) {

            f5.dispose();
            f6.setVisible(true);
        }
        else if (ae.getSource() == finish) {

            f6.dispose();
            f7.setVisible(true);
        }
        else if (ae.getSource() == exit1) {

            f4.dispose();
            f7.setVisible(true);
        }
    }
}
