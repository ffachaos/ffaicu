#!/usr/local/bin/perl --

#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠�͉��L��4�l�ɂ���܂��B
#�����Ȃ闝�R�������Ă����̕\�L���폜���邱�Ƃ͂ł��܂���
#�ᔽ�𔭌������ꍇ�A�X�N���v�g�̗��p���~���Ă�������
#�����łȂ��A�R��ׂ����u�������Ă��������܂��B
#  FF ADVENTURE(������)
#�@remodeling by ����
#�@http://www.eriicu.com
#�@icu@kcc.zaq.ne.jp
#------------------------------------------------------#
#�@FF ADVENTURE ��i v2.1
#�@programed by jun-k
#�@http://www5b.biglobe.ne.jp/~jun-kei/
#�@jun-kei@vanilla.freemail.ne.jp
#------------------------------------------------------#
#�@FF ADVENTURE v0.21
#�@programed by CUMRO
#�@http://cgi.members.interq.or.jp/sun/cumro/mm/
#�@cumro@sun.interq.or.jp
#------------------------------------------------------#
#  FF ADVENTURE(��) v1.021
#  remodeling by GUN
#  http://www2.to/meeting/
#  gun24@j-club.ne.jp
#------------------------------------------------------#

#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
# 3. �ݒu������F����Ɋy����ł��炤�ׂɂ��AWeb�����O�ւ��ЎQ��#
#    ���Ă�������m(__)m						#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi�@		#
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'sankasya.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# ���̃t�@�C���p�ݒ�
$backgif = $sts_back;
$midi = $sts_midi;
#================================================================#
#����������������������������������������������������������������#
#�� �����艺��CGI�Ɏ��M�̂�����ȊO�͈���Ȃ��ق�������ł��@��#
#����������������������������������������������������������������#
#================================================================#

#--------------#
#�@���C�������@#
#--------------#
if ($mente) {
	&error("�o�[�W�����A�b�v���ł��B�Q�A�R�O�b�قǂ��҂��������Bm(_ _)m"); 
}
&decode;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {
		&error("�A�N�Z�X�ł��܂���I�I");
	}
}

&log_in;

#----------------#
#  ���O�C�����  #
#----------------#
sub log_in {

	&chara_load;

	&chara_check;

	&item_load;

	&read_winner;

	$ltime = time();
	$ltime = $ltime - $chara[27];
	$vtime = $b_time - $ltime;
	$xtime = $vtime + 1;
	$ztime = $vtime + 1;
	$mtime = $m_time - $ltime + 1;

	if($chara[28] < $boss) {
		$chara[28] = 0;
	}

	&class;

	if($chara[5]) { $esex = "�j"; } else { $esex = "��"; }
	$next_ex = $chara[18] * $lv_up;

        if(!$chara[32]){$chara[32] = 0;}
	$syou = @shogo[$chara[32]];

        #�h��v�Z
        $yado_daix=int($yado_dai*$chara[18]);

	&header;

	&guest_list;

	&guest_view;

       print <<"EOM";
	<hr size=0>
	<font class=white>���j���[/</font><a href="$scripta?mode=ranking">�o�^�҈ꗗ</a> / <a href="$ranking">�\\�͕ʃ����L���O��</a> / <a href="$syoku_html" target="_blank">�e�E�ƂɕK�v�ȓ����l</a> /<a href="$img_all_list" target="_blank">$vote_gazou</a> /<a href="$bbs" target="_blank">$bbs_title</a> /<a href="$helptext" target="_blank">$helptext_url</a><br>
<font class=white>���̊O��/</font><a href="$sbbs" target="_blank">$sbbs_title</a> / <a href="$vote" target="_blank">$vote_title</a> /<br>
<table align="center"width="100%">
<TR><td rowspan="2"  align="center" class="b2" width=70 height=60><img src="$img_path/$chara_img[$winner[5]]">
<TD id="td1" align="center" colspan=2 class="b2">���݂̃`�����v<a href="$scripta?id=$winner[0]"><B>$winner[3]</B></a>����($winner[44]�A����)</TD></TR>
	<TR><td id="td2"align="center" class="b2">���݂�HP</td><TD class="b2"align="center"><B>$winner[15]\/$winner[16]</B></TD></TR></table>
<hr size=0>

<table border=0 align="center" width='100%'>
<tr>
<td valign=top width='50%'>
EOM
if ($ztime > 0) {
       print <<"EOM";
<table><tr>
<FORM NAME="form1">
<td>
�퓬�J�n�\\�܂Ŏc��<INPUT TYPE="text" NAME="clock" SIZE="3">�b�ł��B(�X�V�̖ڈ��Ɏg���ĉ�����)
</td>
</FORM>
</tr></table>
EOM
}
       print <<"EOM";
<table width="100%">
<tr><td id="td1" colspan="5" class="b2" align="center">�L�����N�^�[�f�[�^</td></tr>
<td rowspan="4" align="center" valign=bottom class="b2"><img src="$img_path/$chara_img[$chara[6]]">
<tr><td id="td2" class="b2">����</td><td align="right" class="b2">$item[0]</td>
<td id="td2" class="b1">�U����</td><td align="right" class="b2">$item[1]</td></tr>
<tr><td id="td2" class="b2">�h��</td><td align="right" class="b2">$item[3]</td>
<td id="td2" class="b1">�h���</td><td align="right" class="b2">$item[4]</td></tr>
<tr><td id="td2" class="b2">�A�N�Z�T���[</td><td align="right" class="b2">$item[6]</td>
	
<td id="td2" class="b2">�̍�</td><td align="center" class="b2"><font color=yellow>$syou</font></td></tr>
</table>

<table width='100%'>
<tr><td id="td1" colspan="5" class="b2" align="center">�X�e�[�^�X</td></tr>
<tr><td class="b1" id="td2">�W���u</td><td class="b2">$chara_syoku[$chara[14]]</td>
<td id="td2" align="center" class="b1">�W���uLV</td><td class="b2"><b>$chara[33]</b></td></tr>
<tr><td class="b1" id="td2">�N���X</td><td colspan=3 class="b2">$class</td></tr>
<tr><td class="b1" id="td2">���x��</td><td class="b2">$chara[18]</td>
<td class="b1" id="td2">�o���l</td><td class="b2">$chara[17]/$next_ex</td></tr>
<tr><td class="b1" id="td2">HP</td><td class="b2">$chara[15]\/$chara[16]</td>
<td class="b1" id="td2">����</td><td class="b2">$chara[19]\/$gold_max</td></tr>
<tr>
<td class="b1" id="td2">�`�����s�I����ڎw��</td>
<form action="$scriptb" method="post">
<td colspan="3" align="center" class="b2">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
EOM
	if ($winner[0] eq $chara[0]) {
		print "���݃`�����v�Ȃ̂œ����܂���\n";
	} elsif ($winner[40] eq $chara[0] and $chanp_milit == 1) {
		print "�`�����v�Ɛ��������Ȃ̂Ŕ��ē����܂���\n";
	}elsif($ltime > $b_time) {
		print "<input type=\"submit\" class=btn value=\"�`�����v�ɒ���\">\n";
	}else{
		print "$ztime�b�㓬����悤�ɂȂ�܂��B\n";
	}
	print <<"EOM";
<br>���܋��F$winner[50] G
</td></form>
</tr>
<tr>
<td class="b1" id="td2" class="b2">�D���ȃL�����Ƒΐ�</td>
<form action="$script_select" method="post">
<td align="center" colspan="3" class="b2">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	if(!$chara[21]) {
		print "�P�x�`�����v�ɒ��킵�Ă�������\n";
	} elsif($ltime > $b_time or !$chara[21]) {
		print "<input type=submit class=btn value=\"�D���ȃL�����ɒ���\">\n";
	} else{
		print "$ztime�b�㓬����悤�ɂȂ�܂��B\n";
	}

	print <<"EOM";
</td></form></tr>
<tr>
<td class="b1" id="td2" class="b2">�V���ꕐ����</td>
<form action="$script_tenka" method="post">
<td align="center" colspan="3" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	if(!$chara[21]) {
		print "�P�x�`�����v�ɒ��킵�Ă�������\n";
	} elsif($ltime > $b_time or !$chara[21]) {
		print "<input type=submit class=btn value=\"�V���ꕐ����\">\n";
	} else{
		print "$ztime�b�㓬����悤�ɂȂ�܂��B\n";
	}

	print <<"EOM";
</td></form></tr>
<tr>
<td class="b1" id="td2">����c��</td>
<form action="$scripts" method="post">
<td colspan="3" align="center" class="b2">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=submit class=btn value="��p�̕ύX">
</td></form>
</tr>
</table>
</td>
EOM

# ��������E�����̃e�[�u��
	print <<"EOM";
<td valign="top">
<table width="100%">
<tr><td id="td1" colspan="4" class="b2" align="center">�X�̎{��</td></tr>
<tr>
<td bgcolor="#cbfffe" align="center">�y���̏h�z(<b>$yado_daix</b>G)</td>
<td bgcolor="#cbfffe" align="center">�y���퉮�z</td>
<td bgcolor="#cbfffe" align="center">�y�h��z</td>
<td bgcolor="#cbfffe" align="center">�y�����i�X�z</td>
</tr>
<tr>
<form action="$scripty" method="post">
<td align="center" class="b2">
<input type=hidden name=mode value="yado">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�̗͂���"></td>
</form>
<form action="$item_shop" method="post">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="���퉮"></td>
</form>
<form action="$def_shop" method="post">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�h�"></td>
</form>
<form action="$acs_shop" method="post">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�����i�X"></td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">�y�X�e�[�^�X�̕ύX�z</td>
<td bgcolor="#cbfffe" align="center">�y��@�s�z</td>
<td bgcolor="#cbfffe" align="center">�y�A�C�e���q�Ɂz</td>
<td bgcolor="#cbfffe" align="center">�y�X�֋ǁz</td>
</tr><tr>
<td align="center" class="b2">
<form action="$scriptst" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X�̕ύX">
</td>
</form>
<form action="$script_bank" method="post">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�@��s�@"></td>
</form>
<form action="$script_souko" method="post">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�A�C�e���q��"></td>
</form>
<form action="$script_post" method="post">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�֋�">
</td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">�y�]�E�̐_�a�z</td>
<td bgcolor="#cbfffe" align="center">�y�X�n�z</td>
<td bgcolor="#cbfffe" align="center">�y�X�n�z</td>
<td bgcolor="#cbfffe" align="center">�y�X�V���z</td>
</tr><tr>
<form action="$script_tensyoku" method="post">
<td align="center" class="b2">
<input type=hidden name=mode value=tensyoku>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�]�E�̐_�a">
</td>
</form>
<td align="center" class="b2">
�X�n
</td>
<td align="center" class="b2">
�X�n
</td>
<form action="$script" method="post">
<td align="center" class="b2">
<input type=hidden name=mode value=log_in>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="��ʍX�V">
</td>
</form>
</tr>
</table>
<table width="100%">
<tr>
<td id="td1" colspan="2" class="b2" align="center">�`���ɏo������</td>
</tr>
<tr><td class="b1" id="td2">
���ӂ̒T��</td>
<form action="$scriptm" method="post">
<td align="center" class="b2">
<input type=hidden name=mode value=monster>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM

	if(!$chara[21]) {
		print "�P�x�`�����v�ɒ��킵�Ă�������\n";
	} elsif($ltime >= $m_time or !$chara[21]) {
	print <<"EOM";
<select name="mons_file">
<option value="monster0">���̕ӂɏo������i�ア�G���o���I�j
<option value="monster1">�߂��̓��A�i�����G���o���I�j
<option value="monster2">�_�[�N�_���W�����i���Ȃ苭���G���o���I�j
<option value="monster3">�~�V�f�B�A�̓��i�S�̂悤�ȓG���o���I�j
</select>
<input type=submit class=btn value="�����X�^�[�Ɠ���">
EOM
	}else{
		print "$mtime�b�㓬����悤�ɂȂ�܂��B<br>\n";
	}

	print <<"EOM";
</td>
</form>
</tr><tr><td colspan=2>���C�s�̗��ɂ����܂��B</td></tr>
EOM

	if($chara[27]%5 == 0){
	print <<"EOM";
<tr><td class="b1" id="td2">�ˑR�̏o��</td>
<form action=\"$scriptm\" method=\"post\">
<td align=\"center\" class=\"b2\">
<input type=hidden name=mode value=genei>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	if (!$chara[21]) {
		print "�P�x�`�����v�ɒ��킵�Ă�������\n";
	} elsif($ltime >= $m_time or !$chara[21]) {
	print "<input type=submit class=btn value=\"���e�̏��\">\n";
	} else {
		print "$mtime�b��s����悤�ɂȂ�܂��B<br>\n";
	}

	print <<"EOM";
</td>
</form>
</tr><tr><td colspan=2>
�����󂪖���ƌ�����u���e�̏�v�ɂ����܂��B
</td></tr>
EOM
}

	print <<"EOM";
<tr>
<td class="b1" id="td2">
���W�F���h�v���C�X</td>
<form action="$script_legend" method="post">
<td align="center" class="b2">
<input type=hidden name=mode value=boss>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	if (!$chara[21] || $chara[28] != $boss) {
		print "�P�x�`�����v�ɒ��킵�Ă�������\n";
	} elsif ($ltime >= $m_time or !$chara[21]) {
		print <<"EOM";
<select name="boss_file">
<option value="0">���킳�̂ق���i���S�҂������J���āE�E�j
EOM
		if ($chara[32] > 0) {
			print "<option value=\"1\">�Â̐_�a�i�n���҂����𗎂Ƃ��Ƃ����E�E�j\n";
		}
		if ($chara[32] > 1) {
			print "<option value=\"2\">�E�҂̓��A�i�`���̗E�҂��K�ꂽ�Ƃ����E�E�j\n";
		}
		if ($chara[32] > 2) {
			print "<option value=\"3\">�K�C�A�t�H�[�X�i�_�݂̂����邱�Ƃ�������Ă���E�E�j\n";
		}
print <<"EOM";
</select>
<input type=submit class=btn value="�`���ɒ���">
EOM
	}else{
		print "$mtime�b�㓬����悤�ɂȂ�܂��B<br>\n";
	}

	print <<"EOM";
</td>
</form>
</tr><tr><td colspan=2>
���ł񂹂̏ꏊ�֖K��邱�Ƃ��ł��܂��B</td></tr>
<tr>
<td class="b1" id="td2">�ِ��E</td>
<form action="$scriptm" method="post">
<td align="center" class="b2">
<input type=hidden name=mode value=isekiai>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	if (!$chara[21]) {
		print "�P�x�`�����v�ɒ��킵�Ă�������\n";
	} elsif ($ltime >= $m_time or !$chara[21]) {
		if ($chara[18] < $isekai_lvl) {
			print "���x����$isekai_lvl�𒴂���܂ōs���܂���B<br>\n";
		} else {
			print "<input type=submit class=btn value=\"�ِ��E�֍s��\"><br>\n";
		}
	} else {
			print "$mtime�b�㓬����悤�ɂȂ�܂��B<br>\n";
	}

	print <<"EOM";
</td></form></tr>
<tr><td colspan=2>���_�X�̗̈�ƌ����邱�̐��E�ɑ����ӂ݂���āA�����ɋA�������̂͒N��l���Ȃ��E�E�E</td></tr>
</table></td></tr></table>
EOM

	&message_load;

	&footer;

	exit;
}
