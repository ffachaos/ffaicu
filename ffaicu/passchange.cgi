#!/usr/local/bin/perl

#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠�͂����ɂ���܂��B
#�����Ȃ闝�R�������Ă����̕\�L���폜���邱�Ƃ͂ł��܂���
#�ᔽ�𔭌������ꍇ�A�X�N���v�g�̗��p���~���Ă�������
#�����łȂ��A�R��ׂ����u�������Ă��������܂��B
#  FF ADVENTURE(������)
#�@edit by ����
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
<form action="$script_pass" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="�߂�">
</form>
EOM

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}

if ($mode) { &$mode; }
&namechange;

exit;

#-----------------#
#�@�@�p�X�ύX�@   #
#-----------------#
sub namechange {

	&chara_load;

	&chara_check;

	if ($chara[0] eq 'test') {&error('�e�X�g�L�����͕ύX�ł��܂���');}

	$phit = 0;
	open(IN,"./$pass_folder/$chara[0].cgi") || ($phit = 1);
	@item_new = <IN>;
	close(IN);

	($ppass,$ptan,$ptime,$phost)=split(/<>/,$item_new[0]);

	&get_time($ptime);

	&header;

	print <<"EOM";
<h1>�p�X���[�h�ύX��</h1>
<hr size=0>
<FONT SIZE=3>
EOM
	if (!$phit) {
	print <<"EOM";
<B>�p�X���[�h�ύX�l</B><BR>
�u�N�̃p�X���[�h��ύX���Ă����悤�B<br>�p�X���[�h��ύX����ɂ͕ύX�p�P�ꂪ�K�v�����I<br>������Ɗo���Ă��邩�H�ԈႢ������Ƃ��炢�ڂɉ����C������񂾂ȁB�v
</FONT><BR><BR>
<font size=4>���Ȃ��̃p�X���[�h�ύX�́A�O��$gettime��$phost�ɂ���Đݒ肳��܂����B(�������́A�p�X���[�h�ύX�p�ݒ�����̎��ɂ���܂����B)</font><br>
<form action="$script_pass" method="post">
<table><tr><td>
<input type=hidden name=mode value=passchan>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=password name=pass size=10></td><td>�p�X���[�h�m�F����</td></tr>
<tr><td><input type=text name=passchange size=20></td><td>�p�X���[�h�ύX�p�P��</td></tr>
<tr><td><input type=password name=npass size=10></td><td>�V�����p�X���[�h�i�K������������ĖY��Ȃ��悤�ɂ��ĉ������B���p�łS�`�W�����j</td></tr>
<tr><td><input type=password name=nkpass size=10></td><td>�V�����p�X���[�h�̊m�F����</td></tr>
</table>
<input type=submit class=btn value="�p�X���[�h�ύX">
</form>
EOM
	} else {
		print <<"EOM";
<B>�p�X���[�h�ύX�l</B><BR>
�u�N�̃p�X���[�h��ύX���邽�߂̒P���ݒ肵�Ă����悤�B<br>��x�ݒ肵�Ă��܂��Ɠ�x�ƕύX���ł��Ȃ��̂Œ��ӂ��K�v���I<br>�i�V�K�o�^���ɓo�^���Ă����l�͂�����Ɠo�^����Ă��܂���ł����B�\\����Ȃ��ł����A������x�ݒ肨�肢���܂��B�j�v
</FONT><BR><BR>
<form action="$script_pass" method="post">
<table><tr><td>
<input type=hidden name=mode value=$pass_folder>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=password name=pass size=10></td><td>�p�X���[�h�m�F����</td></tr>
<tr><td><input type=text name=$pass_folder size=20></td><td>�p�X���[�h�ύX�p�P��i�K������������ĖY��Ȃ��悤�ɂ��ĉ������B�S�p��4�����`10�����j</td></tr>
</table>
<input type=submit class=btn value="�p�X���[�h�ύX�p�P��ݒ�">
</form>
EOM
	}

	print <<"EOM";
<form action="$script" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

#-----------------#
#�@�@�ύX�p�ݒ�   #
#-----------------#
sub passchange {

	&chara_load;

	&chara_check;

	if ($in{'pass'} ne $chara[1]) {
		&error("�p�X���[�h���Ⴂ�܂��I�I$back_form");
	}

	if ( -e "./$pass_folder/$chara[0].cgi") {
		&error("���łɐݒ肳��Ă��܂��I$back_form");
	}

	&get_host;

	$ntime = time();


	@passchan="$chara[1]<>$in{'passchange'}<>$ntime<>$host<>\n";

	open(OUT,">./$pass_folder/$in{'id'}.cgi");
	print OUT @passchan;
	close(OUT);

	&header;

	print <<"EOM";
<h1>�p�X���[�h�ύX�p�P��̐ݒ�����܂����B</h1><hr>
<br>�p�X���[�h�ύX�p�P��́u<font color=white size=5>$in{'passchange'}</font>�v�͕K���Y��Ȃ��悤�ɂ��ĉ������B
$back_form
<form action="$script" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM
	&footer;

	exit;
}

#-----------------#
#�@�@�ύX�p�ݒ�   #
#-----------------#
sub passchan {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if ($in{'pass'} ne $chara[1]) {
		&error("�p�X���[�h���Ⴂ�܂��I$back_form"); 
	}
	if($in{'passchange'} eq "") {
		&error("�p�X���[�h�ύX�p�P�ꂪ���͂���Ă��܂���I$back_form"); 
	}
	elsif($in{'npass'} eq "") {
		&error("�V�����p�X���[�h�����͂���Ă��܂���I$back_form"); 
	}
	elsif($in{'npass'} ne "$in{'nkpass'}") {
		&error("�p�X���[�h�m�F���͂��Ԉ���Ă��܂��I$back_form");
	}
	elsif(length($in{'npass'})<4 || length($in{'npass'})>8) {
		&error("�p�X���[�h�͂S�`�W�����Őݒ肵�Ă��������I$back_form");
	}

	$lock_file = "$lockfolder/passc$in{'id'}.lock";
	&lock($lock_file,'PSC');
	open(IN,"./$pass_folder/$chara[0].cgi");
	@item_new = <IN>;
	close(IN);

	$hit=0;
	($ppass,$ptan,$ptime,$phost)=split(/<>/,$item_new[0]);

	if ($ptan ne $in{'passchange'}) {
		&error("�p�X���[�h�E�p�X���[�h�ݒ�p�P�ꂪ�Ⴂ�܂��I�I"); 
	}

	&get_host;

	$ntime = time();

	unshift(@item_new,"$in{'npass'}<>$ptan<>$ntime<>$host<>\n");

	open(OUT,">./$pass_folder/$chara[0].cgi");
	print OUT @item_new;
	close(OUT);
	&unlock($lock_file,'PSC');

	$chara[1] = $in{'npass'};

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>�p�X���[�h��ύX���܂����B</h1><hr>
<form action="$script" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}
