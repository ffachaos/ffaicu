#!/usr/local/bin/perl

#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠�͉��L��2�l�ɂ���܂��B
#�����Ȃ闝�R�������Ă����̕\�L���폜���邱�Ƃ͂ł��܂���
#�ᔽ�𔭌������ꍇ�A�X�N���v�g�̗��p���~���Ă�������
#�����łȂ��A�R��ׂ����u�������Ă��������܂��B
#  FF ADVENTURE(������) �Ǘ����[�h�X�N���v�g
#�@remodeling by ����
#�@http://www.eriicu.com
#�@icu@kcc.zaq.ne.jp
#------------------------------------------------------#
# FF BATTLE de i
#�@programed by jun-k
#�@http://www5b.biglobe.ne.jp/~jun-kei/
#�@jun-kei@vanilla.freemail.ne.jp
#------------------------------------------------------#

#------------------------------------------------------#
# �{�X�N���v�g�̍쐬�҂͂����ł����A�X�N���v�g�̒��쌠��CUMRO����
# �ɂ���܂��A�K�v�Ȓ��쌠�\�����������Ďg�p���邱�Ƃ͂ł��܂���
# �{�X�N���v�g�Ɋւ��Ă̂��₢���킹�͂����܂ł��肢���܂��B
# CUMRO�ɂ͐�΂ɂ��Ȃ��ŉ������B
#------------------------------------------------------#

#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi		#
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';
$java_script_temp = $java_script;
$java_script = "";

# �Ǘ��l���[�h�̃p�X���[�h
$kanripass = '1111';

# �L�����ʕۑ��p�t�H���_��(�폜�p)
$data_folder[0] = "./charalog";
$data_folder[1] = $message_file;
$data_folder[2] = $ban_file;
$data_folder[3] = "$souko_folder/acs";
$data_folder[4] = "$souko_folder/item";
$data_folder[5] = "$souko_folder/def";
$data_folder[6] = "./item";
$data_folder[7] = "./loginlog";
$data_folder[8] = $pass_folder;
$data_folder[9] = "./syoku";
$data_folder[10] = $sousin_file;

#================================================================#
#����������������������������������������������������������������#
#�� �����艺��CGI�Ɏ��M�̂�����ȊO�͈���Ȃ��ق�������ł��@��#
#����������������������������������������������������������������#
#================================================================#

#--------------#
#�@���C�������@#
#--------------#
&decode;
#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}

&get_time(time());

&get_host;

$lock_file = "$lockfolder/ad.lock";
&lock($lock_file,'AD');
open(IN,"./kanrilog.cgi");
@logindata = <IN>;
close(IN);

$logins=@logindata;

if($logins >= 20){pop(@logindata);}

unshift(@logindata,"$in{'pass'}<>$host<>$gettime<>\n");

open(OUT,">./kanrilog.cgi");
print OUT @logindata;
close(OUT);
&unlock($lock_file,'AD');

if ($in{'pass'} ne $kanripass) { &error('�p�X���[�h����͂��ĉ�����'); }

$back_form = << "EOM";
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�߂�">
</form>
EOM

if ($mode) { &$mode; }
&kanri_top;
exit;

#-----------------#
#  �Ǘ��l���[�h   #
#-----------------#
sub kanri_top {


	$ima = time();
	$sousu = @RANK_NEW;

	&header;

	print <<"EOM";
<h1>�Ǘ����[�h</h1><hr size=0>
�����ݓo�^����Ă���L�����N�^�[���v���C�p�x���������ɕ\\�����Ă��܂��B<br>
����U<b>�폜</b>����ƁA��x�ƕ����ł��Ȃ��Ȃ�̂ŕK��<b>�o�b�N�A�b�v</b>���Ƃ��Ă�����s���Ă��������B<br><br>
�����ŋ߂̊Ǘ����[�h�g�p�̗���(�����s�����N�����x�Ƀ��O���擾���Ă��܂�)
<table bgcolor="#000000" cellspacing="1">
<tr><th>���O�C������</th><th>�z�X�g</th><th>���̓p�X���[�h</th></tr>
EOM
	foreach (@logindata) {
		($pass,$host,$time) = split(/<>/);
		if ($pass eq $kanripass) { print "<tr bgcolor=\"#eeeeee\">"; }
		else { print "<tr bgcolor=\"#ffaaaa\">"; }
		print "<td align=center>$time</td><td align=center>$host</td><td align=center>$pass</td></tr>";
		
	}
	print <<"EOM";
</table>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value=del_noplay>
<input type=submit class=btn value="�v���C�������߂����L�����N�^�[�f�[�^�̊��S�폜"><br>
(�O��퓬����퓬������$limit���o�߂��Ă��܂����L�����������I�ɍ폜���܂�)
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value=kanri_all>
<input type=submit class=btn value="�L�����N�^�[�ꗗ"><br>
(�e�e�`���̃L�����N�^�[���ꗗ�ŕ\\�����܂�)
</form>
<form action="$scriptk" method="post">
<input type="text" name=id size=20>
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value=data>
<input type=submit class=btn value="�h�c�w��L�����N�^�[�f�[�^"><br>
(�e�e�`���̃L�����N�^�[����h�c�Ō������āA�ڍׂȃf�[�^��\\�����܂�)
</form>
<form action="$scriptk" method="post">
<input type="text" name=name size=20>
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value=data>
<input type=submit class=btn value="���O�w��L�����N�^�[�f�[�^"><br>
(�e�e�`���̃L�����N�^�[���疼�O�Ō������āA�ڍׂȃf�[�^��\\�����܂�)
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value=save>
<input type=submit class=btn value="�L�����ۑ�"><br>
(�폜�����o�߂��Ă��폜����Ȃ��L�����N�^�[���w�肵�܂�)
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value=img>
<input type=submit class=btn value="�摜�̒ǉ�"><br>
(./images/chara�t�H���_���̉摜�������I�ɓǂݎ��Affadventure.ini�ɒǉ�����p�Ɉꗗ�ŏo�͂��܂��B<br>HTML��CGI����������Ă���T�[�o�[�ł��g�p�ł��܂��̂ŁA�摜��ǉ�����ۂȂǂɈꎞ�I�ɉ摜�����A�ꗗ���o�͂���ƕ֗��ł��B)
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="syoku">
<input type=submit class=btn value="�E�Ƃ̕ҏW"><br>
(�E�ƕʂׂ̍����ݒ��ύX�ł��܂��B)
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="item_all">
<input type=submit class=btn value="�A�C�e���ꗗ"><br>
(�A�C�e���̈ꗗ������܂��B)
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="waza_all">
<input type=submit class=btn value="�K�E�Z�ꗗ"><br>
(�K�E�Z�̈ꗗ������܂��B)
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="syoku_add_pre">
<input type=submit class=btn value="�E�Ƃ̒ǉ�"><br>
(�E�ƒǉ��̏������ł��܂��B)
</form>
<br>
<br>
<br>
<br>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value=del_all><br>
<input type=submit class=btn value="�S���O�f�[�^�̍폜"><br>
(�e�e�`���̑S�L�����N�^�[�f�[�^�𖕏����܂�)
</form>
EOM
	&footer;

	exit;

}

#-----------------#
#  �Ǘ��l���[�h   #
#-----------------#
sub kanri_all {


	opendir(DIR,'./charalog') or die "$!";
	foreach $entry (readdir(DIR)){

		if($entry=~/\.cgi/){
			open(IN,"./charalog/$entry");
			$WORK=<IN>;
			push(@RANK_NEW,"$WORK\n");
			close(IN);
		}
	}
	closedir(DIR);
	
	@tmp = ();
	if($in{'list'} eq 'other_list') {
		# �z��28�ԖڂŃ\�[�g
		@tmp = map {(split /<>/)[21]} @RANK_NEW;
	}elsif($in{'list'} eq 'ip_list') {
		# �z��28�ԖڂŃ\�[�g
		@tmp = map {(split /<>/)[26]} @RANK_NEW;
	}else{
		# �z��28�ԖڂŃ\�[�g
		@tmp = map {(split /<>/)[27]} @RANK_NEW;
	}

	@RANK_NEW = @RANK_NEW[sort {$tmp[$b] <=> $tmp[$a] } 0 .. $#tmp];

	$ima = time();
	$sousu = @RANK_NEW;

	&header;

	print <<"EOM";
<h1>�Ǘ����[�h</h1><hr size=0>
�����ݓo�^����Ă���L�����N�^�[��\\�����Ă��܂��B<br>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value=kanri_all>
<input type=submit class=btn value="���t���ɕ��ёւ�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value=kanri_all>
<input type="hidden" name=list value=other_list>
<input type=submit class=btn value="�퓬�񐔏��ɕ��ёւ�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value=kanri_all>
<input type="hidden" name=list value=ip_list>
<input type=submit class=btn value="�h�o�A�h���X���ɕ��ёւ�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=mode value=kanri_top>
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�߂�">
</form>
<hr size=0><p><table border=1>
<tr><th>NO</th><th>���O�C��</th><th>�L������</th><th>�h�c</th><th>�p�X���[�h</th><th>�T�C�g��</th><th>�h�o�A�h���X</th><th>�폜�܂�</th><th>�퓬��</th><th>�폜</th><th>�ۑ�</th><th>�ڍ�</th></tr>
EOM
	$i=1;
	foreach (@RANK_NEW){
		s/\n//;
		s/\r//;
		($rid,$rpass,$rsite,$rurl,$rname,$rsex,$rchara,$rn_0,$rn_1,$rn_2,$rn_3,$rn_4,$rn_5,$rn_6,$rsyoku,$rhp,$rmaxhp,$rex,$rlv,$rgold,$rlp,$rtotal,$rkati,$rwaza,$ritem,$rmons,$rhost,$rdate) = split(/<>/);
		$rdate = $rdate + (60*60*24*$limit);
		$niti = $rdate - $ima;
		$niti = int($niti / (60*60*24));
		if($niti==-11337){$niti_s="<font class=red>���t����</font>";}else{$niti_s="<font class=yellow>$niti</font>��";}

	print <<"EOM";
<tr>
<td align=left>$i</td>
<td align=center valign=center>
<form action="$script" method="post">
<input type=hidden name=mode value=log_in>
<input type=hidden name="id" value="$rid">
<input type=hidden name="mydata" value="$_">
<input type=submit class=btn value="���O�C��">
</td>
<td align=left></form><a href="$scripta?mode=chara_sts&id=$rid">$rname</a></td><td align=left>$rid</td><td align=left>$rpass</td><td align=left><a href=\"$rurl\" target="_blank">$rsite</a></td>
EOM
	if($rhost==$wrhost){$wrhost=$rhost;$rhost="<font class=red>$rhost</font>";}
	print "<td align=left>$rhost</td>";
	print "<td align=left>$niti_s</td>";
	print "<td align=left>$rtotal</td>";

	print <<"EOM";
<form action="$scriptk" method="post">
<td align=center valign=center>
<input type="hidden" name=mode value=del_chara>
<input type=hidden name=id value=$rid>
<input type=hidden name=name value=$rname>
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�폜">
</td></form>
<form action="$scriptk" method="post">
<td align=center valign=center>
<input type="hidden" name=mode value=save_chara>
<input type=hidden name=id value=$rid>
<input type=hidden name=name value=$rname>
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�ۑ�">
</td></form>
<form action="$scriptk" method="post">
<td align=center valign=center>
<input type=hidden name=id value=$rid>
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value=data>
<input type=submit class=btn value="�ڍ�">
</td></form>
EOM
		print "</tr>\n";
		$i++;
	}

	print "</table><p>\n";

	&footer;

	exit;
}

#-----------------#
#  �S���O�폜     #
#-----------------#
sub del_all {

	if(!$in{'kakunin'}) {
		$back_form = << "EOM";
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name="kakunin" value="1">
<input type="hidden" name=mode value=del_all>
<input type=submit class=btn value="�S���O�f�[�^�̍폜">
</form>
<br>
<br>
<br>
<form action="$scriptk" method="post">
<input type=hidden name=mode value=kanri_top>
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�߂�">
</form>
EOM
		&error("�{���ɏ����܂����H$back_form");
	}


	opendir(DIR,'./charalog') or die "$!";
	foreach $entry (readdir(DIR)){

		open(IN,"./charalog/$entry");
		if ($entry =~ /\.cgi/) {
			push(@RANKING,<IN>);
			close(IN);
		}
	}
	closedir(DIR);

	$del_name="";$su=0;
	foreach (@RANKING){
		my @rchara = split(/<>/);
		if($rchara[0] eq "test"){next;}
		$del_name .= "<b>$rchara[4]</b>/";
		$su++;
		&del_file($rchara[0]);
	}

	&all_data_delete;

	&header;

	print <<"EOM";
<h1>���L�̃L�����f�[�^���폜���܂���</h1><hr>
<p>�폜�f�[�^�ꗗ(���v$su��)</font>
$del_name
<form action="$scriptk" method="post">
<input type=hidden name=mode value=kanri_top>
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�߂�">
</form>
EOM

	&footer;

	exit;

}

#------------------------#
#�v���C�����o�߃f�[�^�폜#
#------------------------#
sub del_noplay {

	opendir(DIR,'./charalog') or die "$!";
	foreach $entry (readdir(DIR)){

		if ($entry =~ /\.cgi/) {
			open(IN,"./charalog/$entry");
			push(@RANKING,<IN>);
			close(IN);
		}

	}
	closedir(DIR);

	open(IN,"./save_log.cgi");
	@save_chara = <IN>;
	close(IN);

	$ima = time();

	$del_name="";$su=0;
	foreach (@RANKING){
		$save = 0;
		my @rchara = split(/<>/);
		foreach (@save_chara) {
			s/\n//g;
			s/\r//g;
			@save = split(/<>/);
			if ($save[0] eq $rchara[0]) { $save = 1;last; }
		}
		if ($save) { next; }
		if($rchara[27]){
			$rchara[27] = $rchara[27] + (60*60*24*$limit);
			$niti = $rchara[27] - $ima;
			$niti = int($niti / (60*60*24));
			if ($niti < 0) {
				&del_file($rchara[0]);
				$del_name.="<b>$rchara[4]</b>/";
				$su++;
			}
		} else {
			&del_file($rchara[0]);
			$del_name.="<b>$rchara[4]</b>/";
			$su++;
		}
	}

	&all_data_delete;

	&header;

	print <<"EOM";
<h1>���L�̃L�����f�[�^���폜���܂���</h1><hr>
<p>�폜�f�[�^�ꗗ(���v$su��)</font>
$del_name
<form action="$scriptk" method="post">
<input type=hidden name=mode value=kanri_top>
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�߂�">
</form>
EOM

	&footer;

	exit;

}

#-----------------#
#�L�������O�폜   #
#-----------------#
sub del_chara {

	if(!$in{'kakunin'}) {
		$back_form = << "EOM";
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name="kakunin" value="1">
<input type="hidden" name="id" value="$in{'id'}">
<input type="hidden" name="name" value="$in{'name'}">
<input type="hidden" name=mode value=del_chara>
<input type=submit class=btn value="�폜">
</form>
<br>
<br>
<br>
<form action="$scriptk" method="post">
<input type=hidden name=mode value=kanri_top>
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�߂�">
</form>
EOM
		&error("$in{'name'}�����{���ɏ����܂����H$back_form");
	}

	if($in{'id'} eq ""){&error("�h�c���w�肳��Ă��܂���I�I");}

	&del_file($in{'id'});

	&all_data_delete;

	&header;

	print <<"EOM";
<h1>$in{'name'}�̃��O�f�[�^���폜���܂���</h1><hr>
<form action="$scriptk" method="post">
<input type=hidden name=mode value=kanri_top>
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�߂�">
</form>
EOM

	&footer;

	exit;
}

#--------------------------#
#�w�肵���h�c�̃t�@�C���폜#
#--------------------------#
sub del_file {

	local($id) = @_;
	foreach (@data_folder) {
		$m_charafile="$_/$id.cgi";
		#���O�폜����
		if(-e $m_charafile){unlink($m_charafile);}
	}

	push(@no_data,"$id");
}

#------------------#
#�S�̃t�@�C���̍X�V#
#------------------#
sub all_data_delete{

		opendir (DIR,'./charalog') or die "$!";
		foreach $entry (readdir(DIR)){

			if ($entry =~ /\.cgi/) {
				open(IN,"./charalog/$entry");
				$WORK=<IN>;
				$WORK =~ s/\n//gi;
				$WORK =~ s/\r//gi;
				push(@temp_member,"$WORK\n");
				close(IN);		
			}
		}
		closedir(DIR);

		# �z��19�ԖڂŃ\�[�g
		@tmp = map {(split /<>/)[18]} @temp_member;
		@RANKING = @temp_member[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

		open(OUT,">$all_data_file");
		print OUT @RANKING;
		close(OUT);

}

#-----------------#
#  �Ǘ��l���[�h   #
#-----------------#
sub data {

	if ($in{'name'}) {
		&all_data_read;

		$hit = 0;
		foreach(@RANKING){
			@chara_data = split(/<>/);
			if ($in{'name'} eq $chara_data[4]) { $hit=1;last; }
		}

		$back_form = << "EOM";
<form action=$scriptk method=post>
������x��������
<input type=hidden name=mode value=data>
<input type=hidden name=pass value=$in{'pass'}>
<input type=text name=name size=20>
<input type=submit class=btn value=����>
</form>
<form action=$scriptk method=post>
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value=�߂�>
</form>
EOM

		if(!$hit){&error("�L�����N�^�[��������܂���B$back_form");}
		$in{'id'} = $chara_data[0];
	}

	open(IN,"./charalog/$in{'id'}.cgi");
	$chara_log = <IN>;
	close(IN);

	@chara = split(/<>/,$chara_log);

	$ima = time();

	&header;

	print <<"EOM";
<h1>�Ǘ����[�h</h1><hr size=0>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�߂�">
</form>
<hr size=0><table border=1>
<tr><th>���O�C��</th><th>�L������</th><th>�h�c</th><th>�p�X���[�h</th><th>�ύX�p�P��</th><th>�p�X���[�h�ύX�z�X�g</th><th>�T�C�g��</th><th>�h�o�A�h���X</th><th>�폜�܂�</th><th>�퓬��</th><th>�폜</th><th>�ۑ�</th></tr>
EOM
		$rdate = $chara[27] + (60*60*24*$limit);
		$niti = $rdate - $ima;
		$niti = int($niti / (60*60*24));
		$niti_s="$niti��";
		# �p�X���[�h�f�[�^�擾
		open(IN,"$pass_folder/$chara[0].cgi");
		@pass_data = <IN>;
		close(IN);
		(undef,$i_pass,undef,$phost) = split(/<>/,$pass_data[0]);

		$rhost = "<font class=red>$chara[26]</font>";
	print <<"EOM";
<tr>
<form action="$script" method="post">
<td align=center valign=center>
<input type=hidden name=mode value=log_in>
<input type=hidden name=id value=$chara[0]>
<input type=hidden name="mydata" value="$chara_log">
<input type=submit class=btn value="���O�C��">
</td></form>
<td align=left>
<a href="$scripta?mode=chara_sts&id=$chara[0]">
$chara[4]</a></td>
<td align=left>$chara[0]</td>
<td align=left>
$chara[1]</td>
<td>$i_pass</td>
<td>$phost</td>
<td align=left><a href="$chara[3]" TARGET="_blank">$chara[2]</a></td>
<td align=left>$rhost</td>
<td align=left>$niti_s</td>
<td align=left>$chara[21]</td>
<form action="$scriptk" method="post">
<td align=center valign=center>
<input type="hidden" name=mode value=del_chara>
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�폜">
</td></form>
<form action="$scriptk" method="post">
<td align=center valign=center>
<input type="hidden" name=mode value=save_chara>
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�ۑ�">
</td></form>
</tr></table><br>
EOM

	&message_load;

	require 'sousin.pl';

	&footer;

	exit;

}

#------------#
# �L�����ۑ� #
#------------#
sub save {

	open(IN,"./save_log.cgi");
	@save = <IN>;
	close(IN);

	&header;
	print <<"EOM";
<font size=3>
�����ł̓v���C�����o�߃L�����N�^�[�f�[�^�̊��S�폜�ō폜����Ȃ��L�����N�^�[���w��ł��܂��B<br>
�Ȃ��A�����Ŏw��L�����ł��ʍ폜�͗L���ł��̂ŁA�����Ӊ������B</font>
<form action="$scriptk" method="post">
<input type="text" name="id" size=20>
<input type="hidden" name="pass" value=$in{'pass'}>
<input type="hidden" name=mode value=save_chara>
<input type=submit class=btn value="�h�c�w��ۑ�">
</form>
<form action="$scriptk" method="post">
<TABLE BORDER=0>
<TR>
<TD ALIGN="center" CLASS="b2" id="td1"></TD>
<TD ALIGN="center" CLASS="b2" id="td1">�h�c</TD>
<TD ALIGN="center" CLASS="b2" id="td1">�L������</TD>
</tr>
EOM
	foreach(@save){
		($tid,$tname) = split(/<>/);

		print "<TR><td class=b2 align = center id=td1>\n";
		print "<input type=radio name=id value=$tid></td>\n";
		print "<TD class=b1 align = center>\n";
		print "$tid\n";
		print "</TD>\n";
		print "<TD  class=b1 align = center>\n";
		print "$tname\n";
		print "</TD></tr>\n";
	}
	print <<"EOM";
</table>
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=mode value=save_del>
<input type=submit class=btn value="���X�g����폜">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�߂�">
</form>
EOM

	&footer;

	exit;

}

#------------#
# �L�����ۑ� #
#------------#
sub save_chara {

	&chara_load;

	open(IN,"./save_log.cgi");
	@rank = <IN>;
	close(IN);

	foreach(@rank){
		($sid)=split(/<>/);
		if ($sid eq $chara[0]) {
			$back_form = << "EOM";
<form action="$scriptk" method="post">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="submit" class="btn" value="�߂�">
</form>
EOM
			&error("�o�^�ς݂ł�$back_form");
		}
	}

	push(@rank,"$chara[0]<>$chara[4]<>\n");

	open(OUT,">./save_log.cgi");
	print OUT @rank;
	close(OUT);

	&header;

	print <<"EOM";
$chara[4]�����ۑ��L�������X�g�ɒǉ����܂���<br>
<form action="$scriptk" method="post">
<input type="text" name=id size=20>
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value=save_chara>
<input type=submit class=btn value="�h�c�w��ۑ�">
</form>
<form action="$scriptk" method="post">
<TABLE BORDER=0>
<TR><TD ALIGN="center" CLASS="b2" id="td1"></TD>
<TD ALIGN="center" CLASS="b2" id="td1">�h�c</TD>
<TD ALIGN="center" CLASS="b2" id="td1">�L������</TD>
</tr>
EOM

	foreach(@rank){
		($tid,$tname) = split(/<>/);

		print "<TR><td class=b2 align = center id=td1>\n";
		print "<input type=radio name=id value=$tid></td>\n";
		print "<TD class=b1 align = center>\n";
		print "$tid\n";
		print "</TD>\n";
		print "<TD  class=b1 align = center>\n";
		print "$tname\n";
		print "</TD></tr>\n";
	}
print "</table>";
	print <<"EOM";
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=mode value=save_del>
<input type=submit class=btn value="���X�g����폜">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�߂�">
</form>
EOM

	&footer;

	exit;

}

#----------#
# �ۑ����� #
#----------#
sub save_del {

	open(IN,"./save_log.cgi");
	@rank = <IN>;
	close(IN);

	@ranknew=();
	foreach(@rank){
		($sid)=split(/<>/);
		if($sid ne $in{'id'}){push(@ranknew,"$_");}
	}

	open(OUT,">./save_log.cgi");
	print OUT @ranknew;
	close(OUT);

	&header;

	print <<"EOM";
�������܂���<br>
<form action="$scriptk" method="post">
<input type="text" name=id size=20>
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value=save_chara>
<input type=submit class=btn value="�h�c�w��ۑ�">
</form>
<form action="$scriptk" method="post">
<TABLE BORDER=0>
<TR><TD ALIGN="center" CLASS="b2" id="td1"></TD>
<TD ALIGN="center" CLASS="b2" id="td1">�h�c</TD>
<TD ALIGN="center" CLASS="b2" id="td1">�L������</TD>
</tr>
EOM
	foreach(@ranknew){
		($tid,$tname) = split(/<>/);

		print "<TR><td class=b2 align = center id=td1>\n";
		print "<input type=radio name=id value=$tid></td>\n";
		print "<TD class=b1 align = center>\n";
		print "$tid\n";
		print "</TD>\n";
		print "<TD  class=b1 align = center>\n";
		print "$tname\n";
		print "</TD></tr>\n";
	}

	print <<"EOM";
</table>
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=mode value=save_del>
<input type=submit class=btn value="���X�g����폜">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�߂�">
</form>
EOM

	&footer;

	exit;

}

#----------#
# �摜�ꗗ #
#----------#
sub img {

	$i = 0;
	$s = 0;
	$img_all = "";
	$img_tag[$s] = "<tr>\n";
	$html_link1 = "\[<a href = \"./img_all$s.html\">$s</a>\]";
	opendir(DIR,'./images/chara') or die "$!";
	foreach $entry (readdir(DIR)){


		if ($entry=~/\.(gif|jpg|png|bmp)/) {
			$img_all .= "\$chara_img\[$i\] = \"$entry\"\;<br>\n";
			$img_tag[$s] .= "<td align=\"center\" valign=\"bottom\"><img src=\"$img_path/$entry\"><br>$i</td>\n";
			$i++;
			if ($i % 5 == 0) {
				$img_tag[$s] .= "</tr>\n<tr>\n";
				if ($i % 30 == 0) {
					$s++;
					$img_tag[$s] .= "<tr>";
					$html_link1 .= "\[<a href = \"./img_all$s.html\">$s</a>\]";
				}
			}
		}
	}
	closedir(DIR);

	$s = 0;
	$html_link = "";
	foreach (@img_tag) {
		$html_tag = <<"EOM";
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="Pragma" content="no-cache">
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=Shift_JIS">
<META http-equiv="Content-Script-Type" content="text/javascript">
<META http-equiv="Content-Style-Type" content="text/css">
<SCRIPT Language="JavaScript" src="$java_script_temp" type="text/javascript">
</SCRIPT>
<STYLE type="text/css">
<!--
BODY{
  font-family : $font_name;
  font-size:12px;
  color:$text;
  background-image : url($backgif);
  background-attachment : fixed;
}
.red{font-family : $font_name;color:$red;}
.yellow{font-family : $font_name;color:$yellow;}
.blue{font-family : $font_name;color:$blue;}
.green{font-family : $font_name;color:$green;}
.white{font-family : $font_name;color:$white;}
.dark{font-family : $font_name;color:$dark;}
.small{font-size:8px;$font_name;color:$red;}
//-->
</STYLE>
<link rel="stylesheet" href="$style_sheet" type="text/css">
<title>�摜�ꗗ</title></head>
<body background="$backgif" bgcolor="$bgcolor" text="$text" link="$link" vlink="$vlink" alink="$alink">
<center>
<table border="1">
$img_tag[$s]
</tr>
</table>
�摜�ꗗ�ʃy�[�W<br>
$html_link1
</center>
<HR SIZE=0 WIDTH="100%"><DIV align=right>
FFA ������ver2.00 edit by <a href="http://www.eriicu.com" target="_top">����</a><br>
FFA Emilia Ver1.01 remodeled by Classic(��)<br>
FF Battle De I v3.06 remodeling by <a href="http://www.mj-world.jp/" target="_blank">jun-k</a>(�X�V��~��)<br>
FF ADVENTURE(��) v1.040 remodeled by <a href="http://www.gun-online.com" target="_blank">�f�t�m</a><br>
FF ADVENTURE v0.43 edit by D.Takamiya(CUMRO) <a href="http://www5c.biglobe.ne.jp/~ma-ti/" target="_blank">���z�z��(�Ǘ���ma-ti)</a><br>
</DIV></body></html>
EOM

		open(OUT,">./img_all$s.html");
		print OUT $html_tag;
		close(OUT);
		$html_link .= "<a href = \"./img_all$s.html\" target=\"_blank\">img_all$s.html</a><br>";
		$s++;
	}

	&header;

	print << "EOM";
�ȉ��̃e�[�u������ffadventure.ini�ɂ���w��ӏ��ɃR�s�[�y�[�X�g���ĉ������B<br>
�܂��Affaicu�t�H���_����<br>
$html_link
�Ƃ����t�@�C���쐬����܂����B<br>
�L�����摜�ꗗ���o�͂���Ă���̂ŁA���Ђ����p�������B
<table border="1">
<tr><td>
$img_all
</td></tr>
</table>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�߂�">
</form>
EOM

	&footer;

	exit;
}

#----------#
# �E�ƈꗗ #
#----------#
sub syoku {

	open(IN,"$syoku_file");
	@syoku = <IN>;
	close(IN);

	$syoku_sum = @chara_syoku + 1;

	&header;

	print <<"EOM";
�E�ƈꗗ<br>
<TABLE BORDER=0>
<TR>
EOM
	$s = 0;
	foreach (@chara_syoku) {
		print <<"EOM";
<form action="$scriptk" method="post">
<TD class=b1 align = center>
$chara_syoku[$s]<br>
<input type="hidden" name="syoku" value="$s">
<input type="hidden" name="mode" value="syoku_pre">
<input type=hidden name=pass value=$in{'pass'}>
<input type="submit" class="btn" value="�ύX" size="20">
</TD>
</form>
EOM
		$s++;
		if ($s % 10 == 0) { print "</tr>\n<tr>\n"; }
	}

	print <<"EOM";
</tr>
</table>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�߂�">
</form>
EOM

	&footer;

	exit;

}

#----------#
# �E�Ɣ\�� #
#----------#
sub syoku_pre {

	open(IN,"$syoku_file");
	@syoku = <IN>;
	close(IN);

	@skill = split(/<>/,$syoku[$in{'syoku'}],17);
	@syoku_require = split(/<>/,$skill[16]);
	pop(@skill);

	$syoku_sum = @chara_syoku + 1;

	&header;

	print <<"EOM";
<h1>$chara_syoku[$in{'syoku'}]�\\�͈ꗗ</h1><br>
<form action="$scriptk" method="post">
<input type="hidden" name="syoku" value="$in{'syoku'}">
<input type="hidden" name="mode" value="syoku_change">
<input type=hidden name=pass value=$in{'pass'}>
<TABLE BORDER=0>
<TR>
<TD ALIGN="center" CLASS="b2" id="td1" colspan="8">�]�E�K�{�\\��</TD>
<TD ALIGN="center" CLASS="b2" id="td1" colspan="8">�\\�͏㏸�l</TD>
</tr>
<tr>
<TH><font size=1>��</font></TH>
<TH><font size=1>����</font></TH>
<TH><font size=1>�M�S</font></TH>
<TH><font size=1>������</font></TH>
<TH><font size=1>��p��</font></TH>
<TH><font size=1>����</font></TH>
<TH><font size=1>����</font></TH>
<TH><font size=1>�J���}</font></TH>
<TH><font size=1>��</font></TH>
<TH><font size=1>����</font></TH>
<TH><font size=1>�M�S</font></TH>
<TH><font size=1>������</font></TH>
<TH><font size=1>��p��</font></TH>
<TH><font size=1>����</font></TH>
<TH><font size=1>����</font></TH>
<TH><font size=1>�J���}</font></TH>
</tr>
<tr>
EOM
	
	for ($i=0;$i<=15;$i++) {
		print <<"EOM";
<TD class=b1 align = center>
<input type="text" name="skill$i" value="$skill[$i]" size="4">
</TD>
EOM
	}
			print <<"EOM";
</tr>
</table><br>
<table>
<tr>
<TD ALIGN="center" CLASS="b2" id="td1" colspan="$syoku_sum">
�]�E�K�{�K���E�ƃ��x��
</TD>
</tr>
<tr>
EOM
	$m = 0;
	foreach (@chara_syoku) {
		print "<TH><font size=1>$_</font></TH>";
		print <<"EOM";
<TD class=b1 align = center>
<input type="text" name="master$m" value="$syoku_require[$m]" size="2">
</TD>
EOM
		$m++;
		if ($m % 10 == 0) { print"</tr>\n<tr>\n"; }
	}
	print <<"EOM";
</tr>
</table>
<input type="submit" class="btn" value="$chara_syoku[$in{'syoku'}]�̔\\�͕ύX" size="20">
</form>
<table><tr>
<td valign="top">
<form action="$scriptk" method="post">
���퉮�̔��A�C�e��
<table>
<tr>
<th></th><th>No.</th><th>�Ȃ܂�</th><th>�З�</th><th>���i</th><th>�������␳</th></tr>
EOM
	open(IN,"$item_folder/item$in{'syoku'}.ini");
	@item_array = <IN>;
	close(IN);

	$ino = 0;
	foreach (@item_array) {
		@item = ();
		@item = split(/<>/);
		print <<"EOM";
<tr><td class=b1 align="center">
<input type=radio name=item_no value="$ino">
</td>
EOM
		foreach (@item) {
			print <<"EOM";
<td align=right class=b1>$_</td>
EOM
		}
		print "</tr>\n";
		$ino++;
	}

	print <<"EOM";
</table>
<input type=hidden name=mode value=item_sell>
<input type="hidden" name="syoku" value="$in{'syoku'}">
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=item value=item>
<input type=submit class=btn value="�폜">
</form>
</td><td valign="top">
<form action="$scriptk" method="post">
�h��̔��A�C�e��
<table>
<tr>
<th></th><th>No.</th><th>�Ȃ܂�</th><th>�З�</th><th>���i</th><th>��𗦕␳</th></tr>
EOM
	open(IN,"$def_folder/def$in{'syoku'}.ini");
	@item_array = <IN>;
	close(IN);

	$ino = 0;
	foreach (@item_array) {
		@item = ();
		@item = split(/<>/);
		print <<"EOM";
<tr><td class=b1 align="center">
<input type=radio name=item_no value="$ino">
</td>
EOM
		foreach (@item) {
			print <<"EOM";
<td align=right class=b1>$_</td>
EOM
		}
		print "</tr>\n";
		$ino++;
	}

	print <<"EOM";
</table>
<input type=hidden name=mode value=item_sell>
<input type="hidden" name="syoku" value="$in{'syoku'}">
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=item value=def>
<input type=submit class=btn value="�폜">
</form>
</td></tr></table>
<form action="$scriptk" method="post">
�����i�X�̔��A�C�e��
<table>
<tr>
<th></th><th>No.</th><th>�Ȃ܂�</th><th>���i</th><th>����</th><th>��</th><th>����</th><th>�M�S</th><th>������</th><th>��p��</th><th>����</th><th>����</th><th>�J���}</th><th>������</th><th>���</th><th>�K�E��</th><th>����</th></tr>
EOM
	open(IN,"$acs_folder/acs$in{'syoku'}.ini");
	@item_array = <IN>;
	close(IN);

	$ino = 0;
	foreach (@item_array) {
		@item = ();
		@item = split(/<>/);
		print <<"EOM";
<tr><td class=b1 align="center">
<input type=radio name=item_no value="$ino">
</td>
EOM
		foreach (@item) {
			print <<"EOM";
<td align=right class=b1>$_</td>
EOM
		}
		print "</tr>\n";
		$ino++;
	}

	print <<"EOM";
</table>
<input type=hidden name=mode value=item_sell>
<input type="hidden" name="syoku" value="$in{'syoku'}">
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=item value=acs>
<input type=submit class=btn value="�폜">
</form>
<form action="$scriptk" method="post">
�g�p�\\�K�E�Z<br>
�g�p�����Ƃ́A1�Ń}�X�^�[����Ȃ��Ǝg�p�ł��Ȃ����́A0�Ń}�X�^�[���ĂȂ��Ƃ��g����K�E�Z�ƂȂ�܂��B
<table>
<tr>
<th></th><th>No.</th><th>�Z��</th><th>����</th><th>�g�p����</th></tr>
EOM
	open(IN,"$tac_folder/tac$in{'syoku'}.ini");
	@item_array = <IN>;
	close(IN);

	$ino = 0;
	foreach (@item_array) {
		@item = ();
		@item = split(/<>/);
		print <<"EOM";
<tr><td class=b1 align="center">
<input type=radio name=item_no value="$ino">
</td>
EOM
		foreach (@item) {
			print <<"EOM";
<td align=right class=b1>$_</td>
EOM
		}
		print "</tr>\n";
		$ino++;
	}

	print <<"EOM";
</table>
<input type=hidden name=mode value=item_sell>
<input type="hidden" name="syoku" value="$in{'syoku'}">
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=item value=tac>
<input type=submit class=btn value="�폜">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="syoku">
<input type=submit class=btn value="�E�Ƃ̈ꗗ�ɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�߂�">
</form>
EOM

	&footer;

	exit;

}

#----------#
# �E�ƕҏW #
#----------#
sub syoku_change {

	open(IN,"$syoku_file");
	@syoku = <IN>;
	close(IN);

	$newskill = "";
	for ($i=0;$i<=15;$i++) {
		$hash = "skill$i";
		$newskill .= "$in{$hash}<>";
	}

	$m = 0;
	foreach (@chara_syoku) {
		$hash = "master$m";
		$newskill .= "$in{$hash}<>";
		$m++;
	}

	$syoku[$in{'syoku'}] = "$newskill\n";

	open(OUT,">$syoku_file");
	print OUT @syoku;
	close(OUT);

	&header;

	print <<"EOM";
�ύX���܂���<br>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="syoku">
<input type=submit class=btn value="�E�Ƃ̈ꗗ�ɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;

}

#----------#
# ����폜 #
#----------#
sub item_sell {

	$folder = "$in{'item'}\_folder";

	open(IN,"$$folder/$in{'item'}$in{'syoku'}.ini");
	@item_array = <IN>;
	close(IN);

	splice(@item_array,$in{'item_no'},1);

	open(OUT,">$$folder/$in{'item'}$in{'syoku'}.ini");
	print OUT @item_array;
	close(OUT);

	&header;

	print <<"EOM";
�폜���܂���<br>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="syoku">
<input type=submit class=btn value="�E�Ƃ̈ꗗ�ɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;

}

#----------#
# ����ꗗ #
#----------#
sub item_all {

	&header;

	print <<"EOM";
<h1>�ǂ̃A�C�e�������܂����H</h1>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="item_all_item">
<input type=submit class=btn value="����">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="item_all_def">
<input type=submit class=btn value="�h��">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="item_all_acs">
<input type=submit class=btn value="�����i">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;
}

#----------#
# ����ꗗ #
#----------#
sub item_all_item {

	&header;

	print <<"EOM";
<h1>����ꗗ</h1>
<form action="$scriptk" method="post">
<table>
<tr>
<th></th><th>No.</th><th>�Ȃ܂�</th><th>�З�</th><th>���i</th><th>�������␳</th></tr>
EOM
	open(IN,"$item_file");
	@item_array = <IN>;
	close(IN);

	$ino = 0;
	foreach (@item_array) {
		@item = ();
		@item = split(/<>/);
		print <<"EOM";
<tr><td class=b1 align="center">
<input type=radio name=item_no value="$ino">
</td>
EOM
		foreach (@item) {
			print <<"EOM";
<td align=right class=b1>$_</td>
EOM
		}
		print "</tr>\n";
		$ino++;
	}

	print <<"EOM";
</table>
<input type=hidden name=mode value=item_edit>
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=item value=item>
<input type=submit class=btn value="�ҏW">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=mode value=new_item_edit>
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=item value=item>
<input type=submit class=btn value="�V���������ǉ�����">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;
}

#----------#
# ����ꗗ #
#----------#
sub item_all_def {

	&header;

	print <<"EOM";
<h1>�h��ꗗ</h1>
<form action="$scriptk" method="post">
<table>
<tr>
<th></th><th>No.</th><th>�Ȃ܂�</th><th>�З�</th><th>���i</th><th>��𗦕␳</th></tr>
EOM
	open(IN,"$def_file");
	@item_array = <IN>;
	close(IN);

	$ino = 0;
	foreach (@item_array) {
		@item = ();
		@item = split(/<>/);
		print <<"EOM";
<tr><td class=b1 align="center">
<input type=radio name=item_no value="$ino">
</td>
EOM
		foreach (@item) {
			print <<"EOM";
<td align=right class=b1>$_</td>
EOM
		}
		print "</tr>\n";
		$ino++;
	}

	print <<"EOM";
</table>
<input type=hidden name=mode value=item_edit>
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=item value=def>
<input type=submit class=btn value="�ҏW">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=mode value=new_item_edit>
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=item value=def>
<input type=submit class=btn value="�V�����h���ǉ�����">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;
}

#----------#
# ����ꗗ #
#----------#
sub item_all_acs {

	&header;

	print <<"EOM";
<h1>�����i�ꗗ</h1>
<form action="$scriptk" method="post">
<table>
<tr>
<th></th><th>No.</th><th>�Ȃ܂�</th><th>���i</th><th>����</th><th>��</th><th>����</th><th>�M�S</th><th>������</th><th>��p��</th><th>����</th><th>����</th><th>�J���}</th><th>������</th><th>���</th><th>�K�E��</th><th>����</th></tr>
EOM
	open(IN,"$acs_file");
	@item_array = <IN>;
	close(IN);

	$ino = 0;
	foreach (@item_array) {
		@item = ();
		@item = split(/<>/);
		print <<"EOM";
<tr><td class=b1 align="center">
<input type=radio name=item_no value="$ino">
</td>
EOM
		foreach (@item) {
			print <<"EOM";
<td align=right class=b1>$_</td>
EOM
		}
		print "</tr>\n";
		$ino++;
	}

	print <<"EOM";
</table>
<input type=hidden name=mode value=item_edit>
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=item value=acs>
<input type=submit class=btn value="�ҏW">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=mode value=new_item_edit>
<input type=hidden name=pass value=$in{'pass'}>
<input type=hidden name=item value=acs>
<input type=submit class=btn value="�V���������i��ǉ�����">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;
}

#----------#
# ����ҏW #
#----------#
sub item_edit {

	$file = "$in{'item'}\_file";

	open(IN,"$$file");
	@item_array = <IN>;
	close(IN);

	$item_array[$in{'item_no'}] =~ s/\n//g;
	$item_array[$in{'item_no'}] =~ s/\r//g;

	if ($in{'item'} eq 'acs') {
		$list = '<th>No.</th><th>�Ȃ܂�</th><th>���i</th><th>����</th><th>��</th><th>����</th><th>�M�S</th><th>������</th></tr>';
		$list2 = '<tr><th>��p��</th><th>����</th><th>����</th><th>�J���}</th><th>������</th><th>���</th><th>�K�E��</th><th>����</th></tr>';
	} else {
		$list = '<th>No.</th><th>�Ȃ܂�</th><th>�З�</th><th>���i</th><th>����/��𗦕␳</th></tr>';
	}

	&header;

	@item_data = split(/<>/,$item_array[$in{'item_no'}]);

	print <<"EOM";
<h1>$item_data[1]�̕ҏW</h1>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="item_edit_end">
<input type="hidden" name=item_no value="$in{'item_no'}">
<input type="hidden" name=item value="$in{'item'}">
<input type="hidden" name="item_skill0" value="$item_data[0]">
<table>
$list
<tr>
<td class=b1 align="center">$item_data[0]</td>
EOM
	$i = 0;
	foreach (@item_data) {
		if ($i == 0) { $i++; next; }
		print "<td class=b1><input type=\"text\" name=\"item_skill$i\" value=\"$_\"></td>";
		$i++;
		if ($i == 8) { print "</tr>$list2<tr>"; }
	}

	$i--;

	print <<"EOM";
</tr></table>
<input type="hidden" name="item_num" value="$i">
<input type=submit class=btn value="�\\�͂̕ҏW">
</form>
����̐E�Ƃւ̒ǉ�
<TABLE BORDER=0>
<TR>
EOM
	open(IN,"$syoku_file");
	@syoku = <IN>;
	close(IN);

	$s = 0;
	foreach (@chara_syoku) {
		print <<"EOM";
<form action="$scriptk" method="post">
<TD class=b1 align = center>
$chara_syoku[$s]<br>
<input type="hidden" name="syoku" value="$s">
<input type="hidden" name="mode" value="syoku_item_add">
<input type="hidden" name=item_no value="$in{'item_no'}">
<input type="hidden" name=item value="$in{'item'}">
<input type=hidden name=pass value=$in{'pass'}>
<input type="submit" class="btn" value="���̐E�Ƃɒǉ�" size="20">
</TD>
</form>
EOM
		$s++;
		if ($s % 6 == 0) { print "</tr>\n<tr>\n"; }
	}

	print <<"EOM";
</tr>
</table>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="player_item">
<input type="hidden" name=item_no value="$in{'item_no'}">
<input type="hidden" name=item value="$in{'item'}">
<input type="text" name=id value="">
<input type=submit class=btn value="�v���C���[�̑q�ɂɓ����(ID�w��)">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="item_delete">
<input type="hidden" name=item_no value="$in{'item_no'}">
<input type="hidden" name=item value="$in{'item'}">
<input type=submit class=btn value="���̃A�C�e�����폜����"><br>
(�v���C���[�̑q�ɂ���͂Ȃ��Ȃ�Ȃ��̂ŁA��x���ʂ��n�߂Ă��܂����A�C�e�����폜���邱�Ƃ̓I�X�X���ł��܂���B)
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="item_all">
<input type=submit class=btn value="�A�C�e���̈ꗗ�ɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;

}

#------------------#
# ����t�@�C���ҏW #
#------------------#
sub item_edit_end {

	$file = "$in{'item'}\_file";
	$folder = "$in{'item'}\_folder";

	open(IN,"$$file");
	@item_array = <IN>;
	close(IN);

	$newitem = "";
	for ($i=0;$i<=$in{'item_num'};$i++) {
		$hash = "item_skill$i";
		$newitem .= "$in{$hash}<>";
	}

	$item_array[$in{'item_no'}] = "$newitem\n";

	open(OUT,">$$file");
	print OUT @item_array;
	close(OUT);

	# �E�ƕʂ̓���t�@�C���̓����������ĕϊ�
	opendir (DIR,"$$folder") or die "$!";
	foreach $entry (readdir(DIR)){
		if ($entry =~ /\.ini/) {
			if ($file eq "$folder/$entry") { next; }
			open(IN,"$$folder/$entry");
			@item_data = <IN>;
			close(IN);

			open(OUT,">$$folder/$entry");
			foreach (@item_data) {
				($i_no) = split(/<>/);
				if ($in{'item_skill0'} ne $i_no) {
					print OUT $_;
				} else {
					print OUT "$newitem\n";
				}
			}
			close(OUT);
		}
	}
	closedir(DIR);

	&header;

	print <<"EOM";
�ύX���܂���<br>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=item_no value="$in{'item_no'}">
<input type=hidden name=item value=$in{'item'}>
<input type="hidden" name=mode value="item_edit">
<input type=submit class=btn value="����ڍׂɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="item_all">
<input type=submit class=btn value="�A�C�e���̈ꗗ�ɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;

}

#--------------#
# �E�Ɠ���ǉ� #
#--------------#
sub syoku_item_add {

	$file = "$in{'item'}\_file";
	$folder = "$in{'item'}\_folder";

	open(IN,"$$file");
	@item_array = <IN>;
	close(IN);

	$newitem = $item_array[$in{'item_no'}];

	open(IN,"$$folder/$in{'item'}$in{'syoku'}\.ini");
	@item_data = <IN>;
	close(IN);

	push(@item_data,$newitem);

	# �z��1�ԖڂŃ\�[�g
	@tmp = map {(split /<>/)[0]} @item_data;
	@item_data = @item_data[sort {$tmp[$a] <=> $tmp[$b]} 0 .. $#tmp];

	open(OUT,">$$folder/$in{'item'}$in{'syoku'}\.ini");
	print OUT @item_data;
	close(OUT);

	&header;

	print <<"EOM";
�ύX���܂���<br>
EOM
if ($in{'item'} eq 'tac') {
	print <<"EOM";
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=item_no value="$in{'item_no'}">
<input type="hidden" name=mode value="waza_edit">
<input type=submit class=btn value="�K�E�Z�ڍׂɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="waza_all">
<input type=submit class=btn value="�K�E�Z�̈ꗗ�ɖ߂�">
</form>
EOM
} else {
	print <<"EOM";
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=item_no value="$in{'item_no'}">
<input type=hidden name=item value=$in{'item'}>
<input type="hidden" name=mode value="item_edit">
<input type=submit class=btn value="����ڍׂɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="item_all">
<input type=submit class=btn value="�A�C�e���̈ꗗ�ɖ߂�">
</form>
EOM
}
	print <<"EOM";
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;

}

#----------------------#
# �L�����q�ɂɓ���ǉ� #
#----------------------#
sub player_item {

	$file = "$in{'item'}\_file";

	open(IN,"$$file");
	@item_array = <IN>;
	close(IN);

	$newitem = $item_array[$in{'item_no'}];

	if ($in{'item'} eq 'item') {
		$lock_file = "$lockfolder/sitem$in{'id'}.lock";
		$flock_pre = 'SI';
	} elsif ($in{'item'} eq 'def') {
		$lock_file = "$lockfolder/sdefe$in{'id'}.lock";
		$flock_pre = 'SD';
	} else {
		$lock_file = "$lockfolder/acsesa$in{'id'}.lock";
		$flock_pre = 'SA';
	}

	&lock($lock_file,$flock_pre);
	open(IN,"$souko_folder/$in{'item'}/$in{'id'}.cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item_num = @souko_item;

	if ($souko_item_num >= $item_max) {
		&error("����q�ɂ������ς��ł��I$back_form");
	}

	push(@souko_item,$newitem);

	open(OUT,">$souko_folder/$in{'item'}/$in{'id'}.cgi");
	print OUT @souko_item;
	close(OUT);

	&unlock($lock_file,$flock_pre);


	&header;

	print <<"EOM";
�A�C�e����q�ɂɓ���܂���<br>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=item_no value="$in{'item_no'}">
<input type=hidden name=item value=$in{'item'}>
<input type="hidden" name=mode value="item_edit">
<input type=submit class=btn value="����ڍׂɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="item_all">
<input type=submit class=btn value="�A�C�e���̈ꗗ�ɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;

}

#------------#
# �V����ǉ� #
#------------#
sub new_item_edit {

	$file = "$in{'item'}\_file";

	open(IN,"$$file");
	@item_array = <IN>;
	close(IN);

	if ($in{'item'} eq 'acs') {
		$list = '<th>No.</th><th>�Ȃ܂�</th><th>���i</th><th>����</th><th>��</th><th>����</th><th>�M�S</th><th>������</th></tr>';
		$list2 = '<tr><th>��p��</th><th>����</th><th>����</th><th>�J���}</th><th>������</th><th>���</th><th>�K�E��</th><th>����</th></tr>';
	} else {
		$list = '<th>No.</th><th>�Ȃ܂�</th><th>�З�</th><th>���i</th><th>����/��𗦕␳</th></tr>';
	}

	$data_sum = @item_array - 2;	# �Ō�Q�s�͂Ȃ��p�Ɖ��s�Ȃ���

	$item_array[$data_sum] =~ s/\n//g;
	$item_array[$data_sum] =~ s/\r//g;

	@item_data = split(/<>/,$item_array[$data_sum]);

	$new_no = $item_data[0] + 1;

	$new_no = sprintf("%04d",$new_no);

	&header;

	print <<"EOM";
<h1>�V�����A�C�e���̒ǉ��i$in{'item'}�j</h1>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="new_item_add">
<input type="hidden" name=item value="$in{'item'}">
<input type="hidden" name="item_skill0" value="$new_no">
<table>
$list
<tr>
<td class=b1 align="center">$new_no</td>
EOM
	$i = 0;
	foreach (@item_data) {
		if ($i == 0) { $i++; next; }
		print "<td class=b1><input type=\"text\" name=\"item_skill$i\"></td>";
		$i++;
		if ($i == 8) { print "</tr>$list2<tr>"; }
	}

	$i--;

	print <<"EOM";
</tr></table>
<input type="hidden" name="item_num" value="$i">
<input type=submit class=btn value="�V�����A�C�e����ǉ�����">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="item_all">
<input type=submit class=btn value="�A�C�e���̈ꗗ�ɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;

}

#------------#
# �V����ǉ� #
#------------#
sub new_item_add {

	$file = "$in{'item'}\_file";

	open(IN,"$$file");
	@item_array = <IN>;
	close(IN);

	$newitem = "";
	for ($i=0;$i<=$in{'item_num'};$i++) {
		$hash = "item_skill$i";
		$newitem .= "$in{$hash}<>";
	}

	push(@item_array,"$newitem\n");

	# �z��1�ԖڂŃ\�[�g
	@tmp = map {(split /<>/)[0]} @item_array;
	@item_array = @item_array[sort {$tmp[$a] <=> $tmp[$b]} 0 .. $#tmp];

	open(OUT,">$$file");
	print OUT @item_array;
	close(OUT);

	&header;

	print <<"EOM";
�ǉ����܂���<br>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="item_all">
<input type=submit class=btn value="�A�C�e���̈ꗗ">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="waza_all">
<input type=submit class=btn value="�K�E�Z�̈ꗗ">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;

}

#----------#
# ����폜 #
#----------#
sub item_delete {

	$file = "$in{'item'}\_file";
	$folder = "$in{'item'}\_folder";

	open(IN,"$$file");
	@item_array = <IN>;
	close(IN);

	@item_data = split(/<>/,$item_array[$in{'item_no'}]);

	splice(@item_array,$in{'item_no'},1);

	open(OUT,">$$file");
	print OUT @item_array;
	close(OUT);

	# �E�ƕʂ̓���t�@�C���̓����������č폜
	opendir (DIR,"$$folder") or die "$!";
	foreach $entry (readdir(DIR)){
		if ($entry =~ /\.ini/) {
			if ($file eq "$folder/$entry") { next; }
			open(IN,"$$folder/$entry");
			@item_data = <IN>;
			close(IN);

			open(OUT,">$$folder/$entry");
			foreach (@item_data) {
				($i_no) = split(/<>/);
				if ($item_data[0] eq $i_no) {
					next;
				}
				print OUT $_;
			}
			close(OUT);
		}
	}
	closedir(DIR);

	&header;

	print <<"EOM";
�폜���܂���<br>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="item_all">
<input type=submit class=btn value="�A�C�e���̈ꗗ">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="waza_all">
<input type=submit class=btn value="�K�E�Z�̈ꗗ">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;

}

#------------#
# �V�E�ƒǉ� #
#------------#
sub syoku_add_pre {

	$syoku_sum = @chara_syoku;
	$next_syoku = $syoku_sum;

	&header;

	print <<"EOM";
<h1>�V�����E�Ƃ̒ǉ�</h1><br>
�V�����E�Ƃ�ǉ����邽�߂̏������s���܂��B<br>
�ȉ��̍��ڂ�S�ċL�����ĉ������B<br>
<b><font color="$yellow" size = 3>�Ȃ��A�����ŊԈႦ���ꍇ�A����pl�t�@�C���Ȃǂ����������Ȃ��Ƃ����Ȃ��̂ŁA�T�d�ɓ��͂��Ă��������悤�ɂ��肢���܂��B</font></b>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="syoku_add" size="40">
�U�����R�����g<br>
�U���̎��ɏo��E�ƕʂ̑䎌�ł��B<br>
<input type=text name="bcomment" value=""><br><br><br>
�U���͔���p�T�u���[�`����<br>
<b><font color="$red" size = 2>syoku�̌�Ɏ��̐����ł���<font color="$yellow" size = 3>$next_syoku</font>�̉p�ꖼ�����ĉ������B<br>������Ԃł�syokuthirty��30�Ԃ̐E�Ƃ̃O�����h�}�X�^�[�p�Ȃ̂ŁA<br>31��syokuthirtyone�Ƃ��������Ɏ��̐����ł���<font color="$yellow" size = 3>$next_syoku</font>�̉p�ꖼ����͂��ĉ������B<br>�K���A���p�������p���œ��͂��ĉ������B<br>�ԈႦ��ƃG���[���o�Ă��܂��܂��B</font></b><br>
<input type=text name="asub" value="syoku" size="20"><br><br><br>
�U���͂ɔ��f������\\�͂̔{��<br>
<b><font color="$red" size = 2>�U���͌���̍ۂ̌v�Z�ŁA�e�����y�ڂ��\\�͂̔{�������߂܂��B<br>0����͂���΂��̔\\�͍͂U���͂֋y�ڂ��܂���B<br>�Q�l�Ƃ��Ă̓O�����h�}�X�^�[�̏ꍇ�͑S�Ă�1�ɂȂ��Ă���܂��B<br>�K���A���p�����œ��͂��ĉ������B<br>�����ł��\\�ł��B<br>�Ȃ��A�S�̂Ƃ����͕̂���ȊO�̑S�Ă̐��l�𑫂������Ƃɂ����鐔�l�ɂȂ�܂��B<br>�Ǘ��l�Ȃǂ̐E�Ƃł�2�ɂȂ��Ă���܂��B</font></b><br>
<table bgcolor="#ffffff">
<tr><th>��</th><th>����</th><th>�M�S</th><th>������</th><th>��p��</th><th>����</th><th>����</th><th>�S��</th><th>����</th></tr>
<tr>
<td align="center"><input type=text name="a1" value="0" size="5"></td>
<td align="center"><input type=text name="a2" value="0" size="5"></td>
<td align="center"><input type=text name="a3" value="0" size="5"></td>
<td align="center"><input type=text name="a4" value="0" size="5"></td>
<td align="center"><input type=text name="a5" value="0" size="5"></td>
<td align="center"><input type=text name="a6" value="0" size="5"></td>
<td align="center"><input type=text name="a7" value="0" size="5"></td>
<td align="center"><input type=text name="at" value="0" size="5"></td>
<td align="center"><input type=text name="ai" value="0" size="5"></td>
</tr>
</table><br>
<input type=submit class=btn value="�V�����E�Ƃ�ǉ�����">
</form>
<hr>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;

}

#----------#
# �E�ƒǉ� #
#----------#
sub syoku_add {

	if ($in{'a1'} =~ /[^0-9]/ || $in{'a2'} =~ /[^0-9]/ || $in{'a3'} =~ /[^0-9]/ || $in{'a4'} =~ /[^0-9]/ || $in{'a5'} =~ /[^0-9]/ || $in{'a6'} =~ /[^0-9]/ || $in{'a7'} =~ /[^0-9]/ || $in{'at'} =~ /[^0-9]/ || $in{'ai'} =~ /[^0-9]/ || $in{'asub'} =~ /[^_a-z]/) {
		&error("�K���ɂ����Ă��Ȃ����͒l������܂����B$back_form");
	}

	if ($in{'a1'} eq "" || $in{'a2'} eq "" || $in{'a3'} eq "" || $in{'a4'} eq "" || $in{'a5'} eq "" || $in{'a6'} eq "" || $in{'a7'} eq "" || $in{'at'} eq "" || $in{'ai'} eq "" || $in{'asub'} eq "" || $in{'bcomment'} eq "") {
		&error("���͂���Ă��Ȃ����ڂ�����܂��B$back_form");
	}

	$atacksub = << "EOM";
sub $in{'asub'} {
	\$dmg1 \+\= (int(rand(\$chara\[7\] \* $in{'a1'})) \+ int(rand(\$chara\[8\] \* $in{'a2'})) \+ int(rand(\$chara\[9\] \* $in{'a3'})) \+ int(rand(\$chara\[10\] \* $in{'a4'})) \+ int(rand(\$chara\[11\] \* $in{'a5'})) \+ int(rand(\$chara\[12\] \* $in{'a6'})) \+ int(rand(\$chara\[13\] \* $in{'a7'})) \+ int(\$chara\[20\])) \* $in{'at'} \+ \$item\[1\] \* $in{'ai'}\;
}
EOM
chomp($atacksub);

	$watacksub = << "EOM";
sub w$in{'asub'} {
	\$dmg2 \+\= (int(rand(\$winner\[6\] \* $in{'a1'})) \+ int(rand(\$winner\[7\] \* $in{'a2'})) \+ int(rand(\$winner\[8\] \* $in{'a3'})) \+ int(rand(\$winner\[9\] \* $in{'a4'})) \+ int(rand(\$winner\[10\] \* $in{'a5'})) \+ int(rand(\$winner\[11\] \* $in{'a6'})) \+ int(rand(\$winner\[12\] \* $in{'a7'})) \+ int(\$winner\[13\]))  \* $in{'at'} \+ \$winner\[22\] \* $in{'ai'}\;
}
EOM
chomp($watacksub);

	open(IN,"./battle.pl");
	@new = ();
	foreach (<IN>) {
		$_ =~ s/\"\)\;\#�R�����g/\"\,\n\t\"$in{'bcomment'}\"\)\;\#�R�����g/i;
		$_ =~ s/\'\)\;\#�E�ƕʍU���͌��肱���܂�/\'\,\'$in{'asub'}\'\)\;\#�E�ƕʍU���͌��肱���܂�/i;
		$_ =~ s/\}\#�U���͌v�Z�����܂�/\}\n$atacksub\#�U���͌v�Z�����܂�/i;
		push(@new,$_);
	}
	close(IN);

	open(OUT,">./battle.pl");
	print OUT @new;
	close(OUT);

	open(IN,"./wbattle.pl");
	@new = ();
	foreach (<IN>) {
		$_ =~ s/\}\#�`�����v�U���͌v�Z�����܂�/\}\n$watacksub\#�`�����v�U���͌v�Z�����܂�/i;
		push(@new,$_);
	}
	close(IN);

	open(OUT,">./wbattle.pl");
	print OUT @new;
	close(OUT);

	$syoku_sum = @chara_syoku - 1;
	$next_syoku = $syoku_sum + 1;

	&header;

	print <<"EOM";
�E�ƒǉ������������܂���<br>
ffadventure.ini����<br>
\$chara_syoku[$syoku_sum] = \"$chara_syoku[$syoku_sum]\"\;<br>
�̉���<br>
\$chara_syoku[$next_syoku] = \"�V�����E�Ɩ�\"\;<br>
��ǉ����ĉ������B<br>
�ǉ���A�E�Ƃ̕ҏW�ōׂ����ڍׂ����肷��ΐE�Ƃ̒ǉ����������܂�<br>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="syoku_add_pre">
<input type=submit class=btn value="�E�Ƃ̒ǉ��ɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;

}

#--------#
# �Z�ꗗ #
#--------#
sub waza_all {

	&header;

	print <<"EOM";
<h1>�Z�ꗗ</h1><br>
<form action="$scriptk" method="post">
�g�p�����Ƃ́A���̕K�E�Z���g�p����̂Ɍ��݂̐E�Ƃ��}�X�^�[�ł���K�v�����邩�ǂ������������̂ŁA�}�X�^�[����Ȃ��Ǝg�p�ł��Ȃ����̂�1�A�}�X�^�[�łȂ��Ƃ��g�p�ł���̂�0�Ƃ��ĕ\\������Ă��܂��B<br>
<table>
<tr>
<th></th><th>No.</th><th>�Z��</th><th>����</th><th>�g�p����</th></tr>
EOM
	open(IN,"$tac_file");
	@item_array = <IN>;
	close(IN);

	$ino = 0;
	foreach (@item_array) {
		@item = ();
		@item = split(/<>/);
		print <<"EOM";
<tr><td class=b1 align="center">
<input type=radio name=item_no value="$ino">
</td>
EOM
		foreach (@item) {
			print <<"EOM";
<td align=right class=b1>$_</td>
EOM
		}
		print "</tr>\n";
		$ino++;
	}

	print <<"EOM";
</table>
<input type=hidden name=mode value=waza_edit>
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�ҏW">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=mode value=new_waza_edit>
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�V�����K�E�Z��ǉ�����">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;
}

#----------#
# �V�Z�ǉ� #
#----------#
sub new_waza_edit {

	open(IN,"$tac_file");
	@item_array = <IN>;
	close(IN);

	$data_sum = @item_array - 1;	# �Ō�Q�s�͂Ȃ��p�Ɖ��s�Ȃ���

	$item_array[$data_sum] =~ s/\n//g;
	$item_array[$data_sum] =~ s/\r//g;

	@item_data = split(/<>/,$item_array[$data_sum]);

	$new_no = $item_data[0] + 1;

	&header;

	print <<"EOM";
<h1>�V�����K�E�Z�̒ǉ�</h1><br>
�܂��́A�K�E�Z�p�̐V�����t�@�C�����_�E�����[�h���Ă��ĉ������B<br>
<a href="http://www.eriicu.com" target="_blank">�����̂b�f�h�̂g�o</a><br>
����𒧐�җp�̃t�@�C������<br>
$new_no.pl<br>
�Ƃ���tech�t�H���_�ɓ���ĉ������B<br>
�`�����v�p�̃t�@�C����<br>
$new_no.pl<br>
�Ƃ���wtech�t�H���_�ɓ���ĉ������B<br>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="new_item_add">
<input type="hidden" name=item value="tac">
<input type="hidden" name="item_skill0" value="$new_no">
<table>
<tr>
<th>No.</th><th>�K�E�Z��</th><th>����</th><th>�g�p����</th>
</tr>
<tr>
<td class=b1 align="center">$new_no</td>
EOM
	$i = 0;
	foreach (@item_data) {
		if ($i == 0) { $i++; next; }
		print "<td class=b1><input type=\"text\" name=\"item_skill$i\"></td>";
		$i++;
		if ($i == 8) { print "</tr>$list2<tr>"; }
	}

	$i--;

	print <<"EOM";
</tr></table>
<input type="hidden" name="item_num" value="$i">
<input type=submit class=btn value="�V�����K�E�Z��ǉ�����">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="waza_all">
<input type=submit class=btn value="�K�E�Z�̈ꗗ�ɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;

}

#--------#
# �Z�ҏW #
#--------#
sub waza_edit {

	open(IN,"$tac_file");
	@item_array = <IN>;
	close(IN);

	$item_array[$in{'item_no'}] =~ s/\n//g;
	$item_array[$in{'item_no'}] =~ s/\r//g;

	&header;

	@item_data = split(/<>/,$item_array[$in{'item_no'}]);

	print <<"EOM";
<h1>$item_data[1]�̕ҏW</h1>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="waza_edit_end">
<input type="hidden" name=item_no value="$in{'item_no'}">
<input type="hidden" name="item_skill0" value="$item_data[0]">
<table>
<tr>
<th>No.</th><th>�K�E�Z��</th><th>����</th><th>�g�p����</th>
</tr>
<tr>
<td class=b1 align="center">$item_data[0]</td>
EOM
	$i = 0;
	foreach (@item_data) {
		if ($i == 0) { $i++; next; }
		print "<td class=b1><input type=\"text\" name=\"item_skill$i\" value=\"$_\"></td>";
		$i++;
	}

	$i--;

	print <<"EOM";
</tr></table>
<input type="hidden" name="item_num" value="$i">
<input type=submit class=btn value="�K�E�Z�̕ҏW">
</form>
����̐E�Ƃւ̒ǉ�
<TABLE BORDER=0>
<TR>
EOM
	open(IN,"$syoku_file");
	@syoku = <IN>;
	close(IN);

	$s = 0;
	foreach (@chara_syoku) {
		print <<"EOM";
<form action="$scriptk" method="post">
<TD class=b1 align = center>
$chara_syoku[$s]<br>
<input type="hidden" name="syoku" value="$s">
<input type="hidden" name="mode" value="syoku_item_add">
<input type="hidden" name="item_no" value="$in{'item_no'}">
<input type="hidden" name="item" value="tac">
<input type=hidden name=pass value=$in{'pass'}>
<input type="submit" class="btn" value="���̐E�Ƃɒǉ�" size="20">
</TD>
</form>
EOM
		$s++;
		if ($s % 6 == 0) { print "</tr>\n<tr>\n"; }
	}

	print <<"EOM";
</tr>
</table>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="item_delete">
<input type="hidden" name=item_no value="$in{'item_no'}">
<input type="hidden" name=item value="tac">
<input type=submit class=btn value="���̋Z���폜����"><br>
(���̕K�E�Z���p�ɐݒ肵�Ă���v���C���[�̕K�E�Z�܂ł͕ύX����܂���B)
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="waza_all">
<input type=submit class=btn value="�K�E�Z�̈ꗗ�ɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;

}

#--------------------#
# �K�E�Z�t�@�C���ҏW #
#--------------------#
sub waza_edit_end {

	open(IN,"$tac_file");
	@item_array = <IN>;
	close(IN);

	$newitem = "";
	for ($i=0;$i<=$in{'item_num'};$i++) {
		$hash = "item_skill$i";
		$newitem .= "$in{$hash}<>";
	}

	$item_array[$in{'item_no'}] = "$newitem\n";

	open(OUT,">$tac_file");
	print OUT @item_array;
	close(OUT);

	# �E�ƕʂ̕K�E�Z�t�@�C���̓����K�E�Z����ĕϊ�
	opendir (DIR,"$tac_folder") or die "$!";
	foreach $entry (readdir(DIR)){
		if ($entry =~ /\.ini/) {
			if ($tac_file eq "$tac_folder/$entry") { next; }
			open(IN,"$tac_folder/$entry");
			@item_data = <IN>;
			close(IN);

			open(OUT,">$tac_folder/$entry");
			foreach (@item_data) {
				($i_no) = split(/<>/);
				if ($in{'item_skill0'} ne $i_no) {
					print OUT $_;
				} else {
					print OUT "$newitem\n";
				}
			}
			close(OUT);
		}
	}
	closedir(DIR);

	&header;

	print <<"EOM";
�ύX���܂���<br>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=item_no value="$in{'item_no'}">
<input type="hidden" name=mode value="waza_edit">
<input type=submit class=btn value="�K�E�Z�ڍׂɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type="hidden" name=mode value="waza_all">
<input type=submit class=btn value="�K�E�Z�̈ꗗ�ɖ߂�">
</form>
<form action="$scriptk" method="post">
<input type=hidden name=pass value=$in{'pass'}>
<input type=submit class=btn value="�Ǘ�TOP�ɖ߂�">
</form>
EOM

	&footer;

	exit;

}

