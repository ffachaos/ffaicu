#!/usr/local/bin/perl --

#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠�͂����ɂ���܂��B
#�����Ȃ闝�R�������Ă����̕\�L���폜���邱�Ƃ͂ł��܂���
#�ᔽ�𔭌������ꍇ�A�X�N���v�g�̗��p���~���Ă�������
#�����łȂ��A�R��ׂ����u�������Ă��������܂��B
#  FF ADVENTURE(������)
#�@remodeling by ����
#�@http://www.eriicu.com
#�@icu@kcc.zaq.ne.jp
#------------------------------------------------------#

#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi             #
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
if($mente) {
	&error("�o�[�W�����A�b�v���ł��B�Q�A�R�O�b�قǂ��҂��������Bm(_ _)m");
}
&decode;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}

&log_in;

#----------------#
#  ���O�C�����  #
#----------------#
sub log_in {

	if (!( -e "./charalog/$in{'id'}.cgi")) {
		&error('ID������������܂���I');
	}

	&chara_load;

if(!@chara) { &error("�L�����f�[�^�������Ă���\\��������܂��B�������܂����H�������A����O�̃o�b�N�A�b�v�f�[�^�ɖ߂邱�ƂɂȂ�܂�<form action=\"hukugen.cgi\" method=\"post\"><input type=hidden name=id value=$in{'id'}><input type=hidden name=mode value=log_in><input type=submit style=\"background-color:#9370DB;color:#FFFFFF;border:2 solid BFEFFF\" value=\"��������\"></form>");}

	&get_host;

	&get_time(time);

	$lock_file = "$lockfolder/login$in{'id'}.lock";
	&lock($lock_file,'LG');

	open(IN,"./loginlog/$in{'id'}.cgi");
	@logindata = <IN>;
	close(IN);

	$logins=@logindata;
	if($logins >= 15){pop(@logindata);}

	if ($in{'pass'} ne $chara[1]) {
			unshift(@logindata,"$in{'pass'}<>$host<>$gettime<>1<>\n");
			open(OUT,">./loginlog/$in{'id'}.cgi");
			print OUT @logindata;
			close(OUT);
			$lock_file = "$lockfolder/login$in{'id'}.lock";
			&unlock($lock_file,'LG');
			&error("�p�X���[�h���Ⴂ�܂��I"); 
	}

	unshift(@logindata,"$in{'pass'}<>$host<>$gettime<>0<>\n");
	open(OUT,">./loginlog/$in{'id'}.cgi");
	print OUT @logindata;
	close(OUT);

	$lock_file = "$lockfolder/login$in{'id'}.lock";
	&unlock($lock_file,'LG');

	$logmiss ="";$logsuc ="";
	foreach(@logindata){
		($logpass,$loghost,$logtime,$lognum)=split(/<>/);
		if($lognum){
			$logmiss .= << "EOM";
<tr>
<td align=center width=40%>$logtime</td>
<td align=center width=30%>$loghost</td>
<td align=center width=30%>$logpass</td>
</tr>
EOM
		} else {
			$logsuc .= << "EOM";
<tr>
<td align=center width=50%>$logtime</td>
<td align=center width=50%>$loghost</td>
</tr>
EOM
		}
	}

	&set_cookie;

	&guest_list;

	&header;

	&guest_view;

       print <<"EOM";
<hr size=0>
<center>
<h1><font color=white><font color=red>$chara[4]</font>�Ń��O�C�����܂���</font></h1>
<table border=0 width=90%><tr><td width=50%>
<table border=1 width=90%>
<tr><td colspan=2 id="td2" align=center class=b2>�ŋ߂̃��O�C����</td></tr>
<tr><td class="b2" align=center>����</td><td class="b2" align=center>�z�X�g</td></tr>
$logsuc
</table></td><td width=50%>
<table border=1 width=90%>
<td colspan=3 id="td2" align=center class=b2>�ŋ߂̃p�X���[�h�G���[���O�C���̏�</td></tr>
<tr><td class="b2" align=center>����</td><td class="b2" align=center>�z�X�g</td><td class="b2" align=center>���̓p�X���[�h</td></tr>
$logmiss
</table></td></tr></table></center>
<br>
<hr size=0>
EOM
	&message_load;

	print"<hr size=0>";

	print <<"EOM";
<center>
<table border=0><tr><td><table border=1>
<tr><td id="td2" align=center class=b2>
<font class="$white">�X�e�[�^�X��ʂ�</font>
</td></tr>
<tr>
<form action="$script" method="POST">
<td align="center">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</td></form></tr></table>
</td></tr></table></center>
EOM

	&footer;

	exit;
}
#------------------#
#  �N�b�L�[�̔��s  #
#------------------#
sub set_cookie {
	# �N�b�L�[��60���ԗL��
	local($sec,$min,$hour,$mday,$mon,$year,$wday) = gmtime(time+60*24*60*60);

	@month=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
	$gmt = sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT",$week[$wday],$mday,$month[$mon],$year+1900,$hour,$min,$sec);

	$cook="id<>$chara[0]\,pass<>$chara[1]";
	print "Set-Cookie: $ffcookie=$cook; expires=$gmt\n";
}

