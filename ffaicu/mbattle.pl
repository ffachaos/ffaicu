#--------------#
#�@�֐��������@#
#--------------#
sub shokika {
	$dmg1 = $chara[18] * (int(rand(5)) + 1);
	$dmg2 = $mdmg + int(rand($mrand));
	$clit1 = "";
	$clit2 = "";
	$sake1 = 0;
	$sake2 = 0;
	$com1 = "";
	$com2 = "$mname���P�����������I�I";
	$kawasi1 = "";
	$kawasi2 = "";
	$hpplus1 = 0;
	$hpplus2 = 0;
	$kaihuku1 = "";
	$kaihuku2 = "";
	$huin = 0;
}

#------------#
#�@HP�̌v�Z�@#
#------------#
sub hp_sum {
	$khp_flg = $khp_flg - $dmg2 - $dmgme1 + $hpplus1;
	if ($khp_flg > $chara[16]) {
		$khp_flg = $chara[16];
	}
	$mhp = $mhp - $dmg1 + $hpplus2;
	if ($mhp > $mhp_flg) {
		$mhp = $mhp_flg;
	}
}

#------------#
#�@���s�����@#
#------------#
sub winlose {
	if ($mhp <= 0) { $win = 1; last; }
	elsif ($khp_flg <= 0) { $win = 0; last; }
	else{ $win = 2; }
}

#------------------#
#�����N���B�e�B�J��#
#------------------#
sub mons_clt{
	#�N���e�B�J�����Z�o
	$kclt_ritu = 100 - int($khp_flg / $chara[16] * 100);
	$mclt_ritu = 100 - int($mhp / $mhp_flg * 100);

	# ���󋅂̌���
	if ($item[7] == 19) {
		if ($mode eq 'boss' or $mode eq 'isekiai') {
	$com1 .= "<font class=\"red\" size=3>$item[6]��������I�I$mname�ɂ͌����Ȃ������I�I</font><br>";
		} else {
			if (int(rand(2))==0) {
				$huin =1;
				$com1 .= "<font class=\"yellow\" size=3>$item[6]��������I�I$mname�̕K�E�Z�𕕂����߂��I�I</font><br>";
			}
		}
	}

	if ($kclt_ritu > int(rand(100))) {
		$com1 .= "<font color=\"$red\" size=5>�N���e�B�J���I�I�u$chara[23]�v</font><br>";
		$dmg1 = $dmg1 * 3;
	}
	if ($mclt_ritu > int(rand(200))) {
		$com2 .= "<font color=\"$red\">�N���e�B�J���I�I</font><br>";
		$dmg2 = $dmg2 + $item[4];
	}
}

#------------------#
#�������          #
#------------------#
sub mons_kaihi{

	#��𗦌v�Z
	$ci_plus = $item[2] + $item[16];
	$cd_plus = $item[5] + $item[17];
	$hit_ritu = int(($chara[11] / 10)+51) + $ci_plus;	

	$sake1 += int(($chara[12] / 20)) + $cd_plus;
	$sake2 += $mkahi - $hit_ritu;

	if ($dmg2 < 0) { $dmg2 = $dmg2; }
	elsif ($dmg2 < $item[4]) { $dmg2 = 0; }
	else{ $dmg2 = $dmg2 - $item[4]; }

	#�E�ƕʖh��{�[�i�X
	if ($chara[14] > 17) { $dmg2 = int($dmg2 / 4); }
	elsif ($ksyoku > 7) { $dmg2 = int($dmg2 / 2); }

	if (int($sake1) > int(rand(300))) {
		$dmg2 = 0;
		$kawasi1 = "<FONT SIZE=4 COLOR=\"$red\">$chara[4]�͐g�����킵���I</FONT>";
	}
	if (int($sake2) > int(rand(100))) {
		$dmg1 = 0;
		$kawasi2 = "<FONT SIZE=4 COLOR=\"$red\">$mname�͐g�����킵���I</FONT>";
	}

}

#------------------#
#�@�퓬��      �@#
#------------------#
sub monsbattle_sts {

	# �\�͒l�o�[�̏ڂ������ݒ�
	$hit_ritu = int(($chara[11] / 10) + 51);
	if ($hit_ritu > 150) { $hit_ritu = 150; }
	$kaihi_ritu = int(($chara[12]/ 20));
	if ($kaihi_ritu > 50) {	$kaihi_ritu = 50; }
	$waza_ritu = int(($chara[20] / 15)) + 10 + $chara[33];
	if ($waza_ritu > 75) { $waza_ritu = 75; }
	$ci_plus = $item[2] + $a_hitup;
	$cd_plus = $item[5] + $a_kaihiup;
	$bwhit   = int(0.5 * ($hit_ritu + $ci_plus));
	$bwkaihi = int(0.5 * ($kaihi_ritu + $cd_plus));
	$bwwaza  = int(1 * ($waza_ritu + $item[18]));
	if ($bwhit > 200) { $bwhit = 200; }
	if ($bwkaihi > 200) { $bwkaihi = 200; }
	if ($bwwaza > 200) { $bwwaza = 200; }

	if ($i == 1) {
		$battle_date[$j] = <<"EOM";
<TABLE BORDER=0>
<TR>
	<TD COLSPAN= "3" ALIGN= "center">
	$i�^�[��
	</TD>
</TR>
<TR>
	<TD ALIGN= "center">
	<IMG SRC= "$img_path/$chara_img[$chara[6]]"><table width= "100%">
<tr><td id= "td2" class= "b2">����</td><td align= "right" class= "b2">$item[0]</td></tr>
<tr><td id= "td2" class= "b2">�h��</td><td align= "right" class= "b2">$item[3]</td></tr>
<tr><td id= "td2" class= "b2">�A�N�Z�T���[</td><td align= "right" class= "b2">$item[6]</td></tr>
<tr><td id= "td2" class= "b2">������</td><td align= "left" class= "b2"><img src=\"$bar\" width=$bwhit height=$bh><br><b>$hit_ritu + $ci_plus%</b></td></tr>
<tr><td id= "td2" class= "b2">���</td><td align= "left" class= "b2"><img src=\"$bar\" width=$bwkaihi height=$bh><br><b>$kaihi_ritu + $cd_plus%</b></td></tr>
<tr><td id= "td2" class= "b2">�K�E��</td><td align= "left" class= "b2"><img src=\"$bar\" width=$bwwaza height=$bh><br><b>$waza_ritu + $item[18]%</b></td></tr>
</table>
	</TD>
	</TR>
<TR>
<TD>
<TABLE>
<TR>
	<TD CLASS= "b1" id= "td2">
	�Ȃ܂�
	</TD>
	<TD CLASS= "b1" id= "td2">
	HP
	</TD>
	<TD CLASS= "b1" id= "td2">
	�E��
	</TD>
	<TD CLASS= "b1" id= "td2">
	LV
	</TD>
</TR>
<TR>
	<TD class= "b2">
	$chara[4]
	</TD>
	<TD class= "b2">
	$khp_flg\/$chara[16]
	</TD>
	<TD class= "b2">
	$chara_syoku[$chara[14]]
	</TD>
	<TD class= "b2">
	$chara[18]
	</TD>
</TR>
</TABLE>
</TD>
<TD>
<FONT SIZE=5 COLOR= "#9999DD">VS</FONT>
</TD>
<TD>
<TABLE>
<TR>
	<TD CLASS= "b1" id= "td2">
	�Ȃ܂�
	</TD>
	<TD CLASS= "b1" id= "td2">
	HP
	</TD>
</TR>
<TR>
	<TD class= "b2">
	$mname
	</TD>
	<TD class= "b2">
	$mhp/$mhp_flg
	</TD>
</TR>
</TABLE>
</TD>
</TR>
</TABLE>
$com1 $clit1 $kawasi2 $mname �� <font class= "yellow">$dmg1</font> �̃_���[�W��^�����B<font class= "yellow">$kaihuku1</font><br><br><br>
$com2 $clit2 $kawasi1 $chara[4] �� <font class= "red">$dmg2</font> �̃_���[�W��^�����B<font class= "yellow">$kaihuku2</font><br><br><br>
EOM
	} else {
		$battle_date[$j] = <<"EOM";
<TABLE BORDER=0>
<TR>
	<TD COLSPAN= "3" ALIGN= "center">
	$i�^�[��
	</TD>
</TR>
<TR>
<TD>
<TABLE>
<TR>
	<TD CLASS= "b1" id= "td2">
	�Ȃ܂�
	</TD>
	<TD CLASS= "b1" id= "td2">
	HP
	</TD>
</TR>
<TR>
	<TD class= "b2">
	$chara[4]
	</TD>
	<TD class= "b2">
	$khp_flg\/$chara[16]
	</TD>
</TR>
</TABLE>
</TD>
<TD>
<FONT SIZE=5 COLOR= "#9999DD">VS</FONT>
</TD>
<TD>
<TABLE>
<TR>
	<TD CLASS= "b1" id= "td2">
	�Ȃ܂�
	</TD>
	<TD CLASS= "b1" id= "td2">
	HP
	</TD>
</TR>
<TR>
	<TD class= "b2">
	$mname
	</TD>
	<TD class= "b2">
	$mhp/$mhp_flg
	</TD>
</TR>
</TABLE>
</TD>
</TR>
</TABLE>
$com1 $clit1 $kawasi2 $mname �� <font class= "yellow">$dmg1</font> �̃_���[�W��^�����B<font class= "yellow">$kaihuku1</font><br><br><br>
$com2 $clit2 $kawasi1 $chara[4] �� <font class= "red">$dmg2</font> �̃_���[�W��^�����B<font class= "yellow">$kaihuku2</font><br><br><br>
EOM
}
}

#------------------#
#�퓬���ʔ���      #
#------------------#
sub sentoukeka{
	if ($win==1) {
		$chara[22] += 1;
		$gold = $mgold + int(rand($mgold)+1);
		$chara[19] += $gold;
		if ($chara[19] > $gold_max) {
			$chara[19] = $gold_max;
		}
		elsif ($chara[19] < 0) {
			$chara[19] = 0;
		}
 		$comment = "<b><font size=5>$chara[4]�́A�퓬�ɏ��������I�I</font></b><br>";
	} elsif ($win==2) {
		$mex = int($mex/2);
		$comment = "<b><font size=5>$chara[4]�́A�����o�����E�E�E��</font></b><br>";
	} else {
		$mex = 1;
		$chara[19] = int(($chara[19] / 100));
		$comment = "<b><font size=5>$chara[4]�́A�퓬�ɕ������E�E�E�B</font></b><br>";
	}
		$chara[17] = $chara[17] + $mex;
		$chara[21] ++;
		$chara[25] --;
		$chara[27] = time();
		$chara[28] = $boss;
}

#------------------#
#�퓬���ʔ���      #
#------------------#
sub legend_sentoukeka{
	if ($win==1) {
		$chara[22] += 1;
		$gold = $mgold + int(rand($mgold)+1);
		$chara[19] += $gold;
		if ($chara[19] > $gold_max) {
			$chara[19] = $gold_max;
		}
		elsif ($chara[19] < 0) {
			$chara[19] = 0;
		}
		$chara[28] -= 1;
		if ($chara[28] == 0) {
			$comment = "<b><font color=yellow size=5>$chara[4]�́A���W�F���h�v���C�X���U�������I�I�V�����̍����^�����܂��I�I</font></b><br>";
			&all_message("$chara[4]���񂪐V���Ƀ��W�F���h�v���C�X���U������A�̍����オ��܂����I");
			if ($chara[32] < $in{'boss_file'} + 1) {
				$chara[32] = $in{'boss_file'} + 1;
			}
		} else {
			$comment = "<b><font size=5>$chara[4]�́A�퓬�ɏ��������I�I�g�o�������񕜂�����</font></b><br>";
		}
	} elsif ($win==2) {
		$mex = int($mex/2);
		$chara[28] = $boss;
		$comment = "<b><font size=5>$chara[4]�́A�����o�����E�E�E��</font></b><br>";
	} else {
		$mex = 1;
		$chara[28] = $boss;
		$chara[19] = int(($chara[19] / 100));
		$comment = "<b><font size=5>$chara[4]�́A�퓬�ɕ������E�E�E�B</font></b><br>";
	}
		$chara[17] = $chara[17] + $mex;
		$chara[21] ++;
		$chara[25] --;
		$chara[27] = time();
}

#--------------#
# ���ԃ`�F�b�N #
#--------------#
sub time_check{
	$ltime = time();
	$ltime = $ltime - $chara[27];
	$vtime = $m_time - $ltime;

	if ($vtime > 0) {
		&error("����$vtime�b�ԓ����܂���B");
	}
}

#----------------------#
# �����X�f�[�^�Ăяo�� #
#----------------------#
sub mons_read{

	($mname,$mex,$mrand,$msp,$mdmg,$mkahi,$monstac,$mons_ritu,$mgold) = split(/<>/,$MONSTER[$r_no]);

	if ($monstac) {
		require "./mons/$monstac.pl";
	} else {
		require "./mons/0.pl";
	}

}

#------------------#
# �퓬��̂g�o���� #
#------------------#
sub hp_after{
	$chara[15] = $khp_flg + int(rand($chara[10]));
	if ($chara[15] > $chara[16]) { $chara[15] = $chara[16]; }
	if ($chara[15] <= 0) { $chara[15] = $chara[16]; }
}

#----------------------#
# �퓬��̃t�b�^�[���� #
#----------------------#
sub mons_footer{
	if ($win) {
		print "$comment $chara[4]�́A$mex�̌o���l����ɓ��ꂽ�B<b>$gold</b>G��ɓ��ꂽ�B<br>\n";
	} else {
		print "$comment $chara[4]�́A$mex�̌o���l����ɓ��ꂽ�B������100����1�ɂȂ����E�E�E(��)<br>\n";
	}

	print <<"EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM
}
1;