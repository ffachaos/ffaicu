#!/usr/local/bin/perl --

#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠�͉��L��3�l�ɂ���܂��B
#�����Ȃ闝�R�������Ă����̕\�L���폜���邱�Ƃ͂ł��܂���
#�ᔽ�𔭌������ꍇ�A�X�N���v�g�̗��p���~���Ă�������
#�����łȂ��A�R��ׂ����u�������Ă��������܂��B
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
#  FF ADVENTURE(������)
#�@remodeling by ����
#�@http://www3.big.or.jp/~icu/
#�@icus2@hotmail.com
#------------------------------------------------------#

#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
# 3. �ݒu������F����Ɋy����ł��炤�ׂɂ��AWeb�����O�ւ��ЎQ��#
#    ���Ă�������m(__)m						#
#     http://www3.big.or.jp/~icu/cgi-bin/cbbs/cbbs.cgi�@		#
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

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

	$back_form = << "EOM";
<br>
<form action="$scriptst" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="�߂�">
</form>
EOM

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {
		&error("�A�N�Z�X�ł��܂���I�I");
	}
}

if ($mode) { &$mode; }
&chara_st;
exit;

#----------------#
#  ���O�C�����  #
#----------------#
sub chara_st {

	&chara_load;

	&chara_check;

	&item_load;

	# �\�͒l�o�[�̏ڂ������ݒ�
	$hit_ritu = int(($chara[11] / 10) + 51);
	if($hit_ritu > 150){$hit_ritu = 150;}
	$kaihi_ritu = int(($chara[12]/ 20));
	if($kaihi_ritu > 50){$kaihi_ritu = 50;}
	$waza_ritu = int(($chara[20] / 15)) + 10 + $chara[33];
	if($waza_ritu > 75){$waza_ritu = 75;}
	$ci_plus = $item[2] + $item[16];
	$cd_plus = $item[5] + $item[18];

	open(IN,"$tac_file");
	@gettac = <IN>;
	close(IN);

	$thit = 0;
	foreach (@gettac) {
		($tacno,$tacname) = split(/<>/);
		if ($chara[30] == $tacno) {
			$ktac_name = $tacname;
			$thit = 1;
			last;
		}
	}

	if (!$thit) { $ktac_name = "���ʂɐ키"; }

	&class;

	if($chara[5]) { $esex = "�j"; } else { $esex = "��"; }
	$next_ex = $chara[18] * $lv_up;

        if(!$chara[32]){$chara[32] = 0;}
	$syou = @shogo[$chara[32]];

	&syoku_load;

	&header;

       print <<"EOM";
<table align="center">
<TR>
<TD><font size=5>$chara[4]����p�X�e�[�^�X�ύX���</font></TD>
</TR>
</table>
<hr size=0>
<font class=white>���j���[/</font>
<a href="$scripta?mode=ranking">�o�^�҈ꗗ</a> / 
<a href="$ranking">\�\\�͕ʃ����L���O��</a> / 
<a href="$syoku_html" target="_blank">�e�E�ƂɕK�v�ȓ����l</a> / 
<a href="$img_all_list" target="_blank">$vote_gazou</a> / 
<a href="$bbs" target="_blank">$bbs_title</a> / 
<a href="$helptext" target="_blank">$helptext_url</a>
<br>
<font class=white>���̊O��/</font>
<a href="$sbbs" target="_blank">$sbbs_title</a> / 
<a href="$vote" target="_blank">$vote_title</a> / 
<br>
<form action="$scripts" method="post">
<table border=0 align="center" width='100%'>
<tr>
<td valign=top width='50%'>
<table width="100%"><tr>
<tr><td id="td1" colspan="5" class="b2" align="center">�L�����N�^�[�f�[�^</td></tr>
<td rowspan="4" align="center" valign=bottom class="b2"><img src="$img_path/$chara_img[$chara[6]]">
<tr><td id="td2" class="b2">����</td><td align="right" class="b2">$item[0]</td>
<td id="td2" class="b1">�U����</td><td align="right" class="b2">$item[1]</td></tr>
<tr><td id="td2" class="b2">�h��</td><td align="right" class="b2">$item[3]</td>
<td id="td2" class="b1">�h���</td><td align="right" class="b2">$item[4]</td></tr>
<tr><td id="td2" class="b2">�A�N�Z�T���[</td><td align="right" class="b2">$item[6]</td>
	
<td id="td2" class="b2">�̍�</td><td align="center" class="b2"><font color=yellow>$syou</font></td></tr>
</table>
<table width="100%">
<tr><td id="td1" colspan="5" class="b2" align="center">�X�e�[�^�X</td></tr>
<tr><td class="b1" id="td2">�W���u</td>
<td class="b2">
$chara_syoku[$chara[14]]
</td>
<td id="td2" align="center" class="b1">�W���uLV</td><td class="b2"><b>$chara[33]</b></td></tr>
<tr><td class="b1" id="td2">�N���X</td><td colspan=3 class="b2">$class</td></tr>
<tr><td class="b1" id="td2">���x��</td><td class="b2">$chara[18]</td>
<td class="b1" id="td2">�o���l</td><td class="b2">$chara[17]/$next_ex</td></tr>
<tr><td class="b1" id="td2">HP</td><td class="b2">$chara[15]\/$chara[16]</td>
<td class="b1" id="td2">����</td><td class="b2">$chara[19]\/$gold_max</td></tr>
</table>

<table width="100%"><tr><td id="td2" align="center" class="b1">���܂ł̃W���u</td></tr>
<tr><td colspan=3 align="center" class="b1">
<table width="100%">
<tr>
EOM
	$s = 0;
	foreach (@syoku_master){
		if ($_) {
			$class_flg = int($syoku_master[$s]/10);
			$class[$s] = $class_mark[$class_flg];
			print "<td class=\"b2\" width=\"20%\" align=\"center\">$chara_syoku[$s]<br>$class[$s]</td>";
		}
		$s++;
		if ($s % 5 == 0) {
			print '</tr><tr>';
		}
	}

	if (!$s) {
		print "<td class=\"b2\" width=\"100%\" align = \"center\">�Ȃ�</td>";
	}

       print <<"EOM";
</tr></table></td></tr></table>
<table width="100%"></form>
<tr><td id="td1" colspan="5" class="b2" align="center">���̑��̃R�}���h</td></tr><tr><td id="td2"align="center" class="b2">�y��p�ύX�z</td>
<form action="$scripts" method="post">
<td align="center"colspan="4" class="b2">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=submit class=btn value="��p��ύX"></td>
</form>
</tr>
<tr><td id="td2"align="center" class="b2">�y�X�e�[�^�X��ʂցz</td>
<form action="$script" method="post">
<td align="center"colspan="4" class="b2">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�"></td>
</form>
</tr>
<tr><td id="td2"align="center" class="b2">�y�p�X���[�h�ύX�z</td>
<form action="$script_pass" method="post">
<td align="center"colspan="4" class="b2">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=submit class=btn value="�p�X���[�h�ύX"></td>
</form>
</tr></table>
<td valign="top">
<table width='100%'>
<form action="$scriptst" method="post">
<tr><td id="td1" colspan="5" class="b2" align="center">�z�[���y�[�W�f�[�^</td></tr>
<tr><td id="td2" class="b1">�z�[���y�[�W��</td></tr><tr><td colspan="4"><input type="text" name=site value="$chara[2]" size=50></td></tr>
<tr><td id="td2" class="b1">�z�[���y�[�W��URL</td></tr><tr><td colspan="4"><input type="text" name=url value="$chara[3]" size=60></td></tr>
</table>
<table width='100%'>
<tr><td id="td1" colspan="5" class="b2" align="center">�X�e�[�^�X</td></tr>
<tr>
<td class="b1" id="td2">�摜�ݒ�</td>
<td class="b2"colspan="4">
<input type="text" name="chara" value="$chara[6]" size=5>
<a href="$img_all_list" target="_blank">
$vote_gazou</a>
</td>
</tr></td>
<tr>
<td class="b1" id="td2">�Ȃ܂�</td><td class="b2">$chara[4]</td>
<td class="b1" id="td2">����</td><td class="b2">$esex</td></tr>
<tr><td class="b1" id="td2">�W���u</td><td class="b2">$chara_syoku[$chara[14]]</td>
<td id="td2" align="center" class="b1">�W���uLV</td><td class="b2"><b>$chara[33]</b></td></tr>
<tr><td class="b1" id="td2">�N���X</td><td colspan=3 class="b2">$class</td></tr>
<tr><td class="b1" id="td2">���x��</td><td class="b2">$chara[18]</td>
<td class="b1" id="td2">�o���l</td><td class="b2">$chara[17]/$next_ex</td></tr>
<tr><td class="b1" id="td2">HP</td><td class="b2">$chara[15]\/$chara[16]</td>
<td class="b1" id="td2">����</td><td class="b2">$chara[19]\/$gold_max</td></tr>
<tr><td class="b1" id="td2">��</td><td align="left" class="b2"><img src=\"$bar\" width=$bw0 height=$bh><br><b>$chara[7] + $item[8]</b></td>
<td class="b1" id="td2">����</td><td align="left" class="b2"><img src=\"$bar\" width=$bw1 height=$bh><br><b>$chara[8] + $item[9]</b></td></tr>
<tr><td class="b1" id="td2">�M�S</td><td align="left" class="b2"><img src=\"$bar\" width=$bw2 height=$bh><br><b>$chara[9] + $item[10]</b></td>
<td class="b1" id="td2">������</td><td align="left" class="b2"><img src=\"$bar\" width=$bw3 height=$bh><br><b>$chara[10] + $item[11]</b></td></tr>
<tr><td class="b1" id="td2">��p��</td><td align="left" class="b2"><img src=\"$bar\" width=$bw4 height=$bh><br><b>$chara[11] + $item[12]</b></td>
<td class="b1" id="td2">����</td><td align="left" class="b2"><img src=\"$bar\" width=$bw5 height=$bh><br><b>$chara[12] + $item[13]</b></td></tr>
<tr><td class="b1" id="td2">����</td><td align="left" class="b2"><img src=\"$bar\" width=$bw6 height=$bh><br><b>$chara[13] + $item[14]</b></td>
<td class="b1" id="td2">�J���}</td><td align="left" class="b2"><img src=\"$bar\" width=$bwlp height=$bh><br><b>$chara[20] + $item[15]</b></td></tr>
<tr><td id="td2" class="b2">������</td><td align="left" class="b2"><img src=\"$bar\" width=$bwhit height=$bh><br><b>$hit_ritu + $ci_plus%</b></td>
<td id="td2" class="b2">���</td><td align="left" class="b2"><img src=\"$bar\" width=$bwkaihi height=$bh><b><br>$kaihi_ritu + $cd_plus%</b></td></tr>
<tr><td id="td2" class="b2">�K�E��</td><td align="left" class="b2"><img src=\"$bar\" width=$bwwaza height=$bh><br><b>$waza_ritu + $item[17]%</b></td><td id="td2" class="b2">�Z��</td><td align="center" class="b2"><B>$ktac_name</B></td></tr>
<tr><td class="b1" id="td2">�Z�������R�����g</td><td colspan="3" align="center" class="b2"><input type="text" name=waza value="$chara[23]" size=50></td></tr>
<tr><td id="td2" class="b1">

�ύX�����X�e�[�^�X��o�^><td align="center" colspan=3 class="b2">
<input type=hidden name=mode value=st_buy>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��o�^����">
</td></tr>
</form>
</table>
</table></td></tr></table>
EOM

	&message_load;

	&footer;

	exit;
}

#----------------#
#  �ύX�o�^���  #
#----------------#
sub st_buy {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	if($in{'id'} eq test){
		&error("�e�X�g�L�����̓X�e�[�^�X�ύX�͂ł��܂���$back_form");
	}

	if($in{'site'} eq "") {
		$in{'site'} = '�����̂b�f�h�̂g�o';
	}
	if($in{'url'} eq "") {
		$in{'url'} = 'http://www.eriicu.com';
	}

	if (length($in{'waza'}) > 100) {
		&error("�N���e�B�J���R�����g���������܂��I$back_form");
	}

	foreach (@ban_word) {
		if(index($in{'waza'},$_) >= 0) {
			$in{'mesname'} = $aite_data[4];
			&error("�֎~��u$_�v���܂܂�Ă��܂�$back_form");
		}
	}

	$chara[2] = $in{'site'};
	$chara[3] = $in{'url'};
	$chara[6] = $in{'chara'};
	$chara[23] = $in{'waza'};

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

 print <<"EOM";
<h1>$chara[4]����̃X�e�[�^�X��ύX���܂���</h1><br>
<form action="$scriptst" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�X�e�[�^�X�ύX��ʂ�">
</form>
EOM

	&footer;

	exit;
}
