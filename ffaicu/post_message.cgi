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
<form action="$script_post" method="post">
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
&messe;

exit;

#--------------#
#  ���b�Z�[�W  #
#--------------#
sub message {

	&chara_load;

	&chara_check;

	if($in{'mes'} eq "") {
		&error("���b�Z�[�W���L������Ă��܂���$back_form");
	}
	elsif($in{'mesid'} eq "" && $in{'mesname'} eq "") {
		&error("���肪�w�肳��Ă��܂���$back_form");
	}
	elsif($in{'id'} eq "test"){
		&error("�e�X�g�L�����ł̓��b�Z�[�W�𑗐M�ł��܂���I$back_form");
	}

	&get_time(time());

	&get_host;

	&all_data_read;

	$mhit = 0;
	foreach (@RANKING) {
		s/\n//gi;
		s/\r//gi;
		@aite_data = split(/<>/);
		if ($aite_data[0] eq $in{'mesid'} || $aite_data[4] eq $in{'mesname'}) {
			$mhit = 1;
			last;
		}
	}

	if ($aite_data[0] eq $chara[0]) {
		&error("�����ɂ̓��b�Z�[�W�𑗐M�ł��܂���I$back_form");
	}

	# ���肪������Ȃ���
	if (!$mhit) {
		&mes_error;
	}

	$now_mes = length($in{'mes'});

	foreach (@ban_word) {
		if(index($in{'mes'},$_) >= 0) {
			$in{'mesname'} = $aite_data[4];
			&error("�\\���͋֎~����Ă��܂�");
		}
	}

	if ($now_mes > $mes_size) {
		$in{'mesname'} = $aite_data[4];
		&res("���b�Z�[�W���������܂��I���p��$mes_size�����܂łł��I(���ݕ������F$now_mes)<br>");
	}

	# ���ۏ�Ԃ̌Ăяo��
	open(IN,"$ban_file/$aite_data[0].cgi");
	@ban_sts = <IN>;
	close(IN);

	$ban_hit = 0;
	foreach (@ban_sts) {
		s/\n//gi;
		s/\r//gi;
		($banid,$bansts) = split(/<>/);
		if ($banid eq 'all'){
			$ban_hit = 1;
		} elsif ($banid eq $chara[0] && $bansts eq 1) {
			# ���ۂ��Ă�l����̃��b�Z�[�W
			$ban_hit = 1;
			last;
		} elsif ($banid eq $chara[0] && $bansts eq 2) {
			# �F�B�o�^���Ă�l����̃��b�Z�[�W
			$ban_hit = 0;
			last;
		}
	}

	if ($ban_hit || $aite_data[0] eq 'test') {
		&error("���b�Z�[�W�������ł�$back_form");
	}

	$lock_file = "$lockfolder/messa$aite_data[0].lock";
	&lock($lock_file,'MS');
	open(IN,"$message_file/$aite_data[0].cgi");
	@mes_regist = <IN>;
	close(IN);

	$mes_sum = @mes_regist;

	if($mes_sum > $mes_max) { pop(@mes_regist); }

	unshift(@mes_regist,"$chara[0]<>$chara[4]<>$gettime<>$in{'mes'}<>$host<>\n");

	open(OUT,">$message_file/$aite_data[0].cgi");
	print OUT @mes_regist;
	close(OUT);
	&unlock($lock_file,'MS');

	$lock_file = "$lockfolder/sousin$chara[0].lock";
	&lock($lock_file,'MS');
	open(IN,"$sousin_file/$chara[0].cgi");
	@sousin = <IN>;
	close(IN);

	$mes_sum = @sousin;

	if($mes_sum > $mes_max) { pop(@sousin); }

	unshift(@sousin,"$aite_data[0]<>$aite_data[4]<>$gettime<>$in{'mes'}<>$host<>\n");

	open(OUT,">$sousin_file/$chara[0].cgi");
	print OUT @sousin;
	close(OUT);
	&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<h1>$aite_data[4]����փ��b�Z�[�W�𑗂�܂����B</h1>
<hr size=0>
<form action="$script_post" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�֋ǂ̍ŏ��̉�ʂ�">
</form>
<form action="$script" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

#------------------#
#���b�Z�[�W�V�X�e��#
#------------------#
sub messe {

	&chara_load;

	&chara_check;

	# �w�b�_�[�\��
	&header;

	print <<"EOM";
<h1>�D���ȃL�����N�^�[�փ��b�Z�[�W�𑗂�</h1>
<hr>�����̃L�����N�^�[�փ��b�Z�[�W�𑗂邱�Ƃ��ł��܂��B
<table width = "100%">
<tr><td class="b2">���O���w�肵�đ���</td>
<form action="$script_post" method="post">
<td class="b2" valign="top">
���O�@�@�@ �F<input type="text" name="mesname" size=10><br>
���b�Z�[�W�F<input type="text" name="mes" size=50><br><br>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value=message>
<input type=submit class=btn value="���b�Z�[�W�𑗂�">
</td>
</form>
<td class="b2" align="left" valign="top" rowspan=2>
EOM

	&message_load;

	require 'sousin.pl';

	print <<"EOM";
</td></tr>
<tr>
<td class="b2">���O��I��ő���</td>
<td class="b2" valign="top">
<br>
<form action="$script_post" method="post">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value=all_list>
<input type=submit class=btn value="�ꗗ���疼�O��I��">
</form>
<form action="$script_post" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="hidden" name="mode" value="ban">
<input type=submit class=btn value="���b�Z�[�W����">
</form>
<form action="$script_post" method="post">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value=friend>
<input type=submit class=btn value="�F�B�o�^">
</form>
<form action="$script_post" method="post">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value="limit">
<input type=submit class=btn value="��M����">
</form>
<form action="$script" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
</td>
</tr></table>
EOM

	&footer;

	exit;
}

#------------------#
#���b�Z�[�W�V�X�e��#
#------------------#
sub all_list {

	&chara_load;

	&chara_check;

	&all_data_read;

	# �z��19�ԖڂŃ\�[�g
	@tmp = map {(split /<>/)[18]} @RANKING;
	@RANKING = @RANKING[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	# �w�b�_�[�\��
	&header;

	print <<"EOM";
<h1>�D���ȃL�����N�^�[�փ��b�Z�[�W�𑗂�</h1>
<hr>�����̃L�����N�^�[�փ��b�Z�[�W�𑗂邱�Ƃ��ł��܂��B
<table>
<tr>
<td class="b2">���b�Z�[�W</td>
<form action="$script_post" method="post">
<td class="b2" valign="top">
<input type="text" name=mes size=50>
</td></tr>
<tr>
<td class="b2">���O�I��</td>
<td class="b2" valign="top">
<select name=mesid size=20>
EOM

	foreach (@RANKING) {
		s/\n//gi;
		s/\r//gi;
		@aite_data = split(/<>/);
		print << "EOM";
<option value = "$aite_data[0]">$aite_data[4]����(Lv.$aite_data[18])��
EOM
	}
	print <<"EOM";
</select>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="hidden" name="mode" value="message">
<input type=submit class=btn value="���b�Z�[�W�𑗂�">
</td>
</form>
</tr></table>
<form action="$script_post" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�֋ǂ̍ŏ��̉�ʂ�">
</form>
<form action="$script" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

#------#
# �ԐM #
#------#
sub res {

	&chara_load;

	&chara_check;

	# �w�b�_�[�\��
	&header;

	print <<"EOM";
<h2>$_[0]</h2>
<h1>$in{'mesname'}����փ��b�Z�[�W�𑗂�</h1>
<form action="$script_post" method="post">
���b�Z�[�W�F<input type="text" name="mes" size=50 value = "$in{'mes'}"><br><br>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type="hidden" name="mesid" value="$in{'mesid'}">
<input type="hidden" name="mesname" value="$in{'mesname'}">
<input type=hidden name=mode value=message>
<input type=submit class=btn value="���b�Z�[�W�𑗂�">
</form>
<form action="$script_post" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�֋ǂ̍ŏ��̉�ʂ�">
</form>
<form action="$script" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

#--------------------#
# ���肪������Ȃ� #
#--------------------#
sub mes_error {

	# �w�b�_�[�\��
	&header;

	print <<"EOM";
<h1>���肪������܂���I</h1>
<form action="$script_post" method="post">
���O�@�@�@ :<input type="text" name="mesname" value="$in{'mesname'}" size="20">
<br>
���b�Z�[�W�F<input type="text" name="mes" size="50" value ="$in{'mes'}">
<br><br>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value=message>
<input type=submit class=btn value="���b�Z�[�W�𑗂�">
</form>
<form action="$script_post" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�֋ǂ̍ŏ��̉�ʂ�">
</form>
<form action="$script" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

#----------#
# ��M���� #
#----------#
sub limit {

	&chara_load;

	&chara_check;

	open(IN,"$ban_file/$chara[0].cgi");
	@ban_sts = <IN>;
	close(IN);

	@new_ban = "";
	$ban_hit = 0;
	@ban_mes = ('����','�ݒ�');
	foreach (@ban_sts) {
		s/\n//gi;
		s/\r//gi;
		($banid,$bansts) = split(/<>/);
		if ($banid eq "all") {
			$ban_hit = 1;
			last;
		}
	}

	# �w�b�_�[�\��
	&header;

	print <<"EOM";
<h1>���b�Z�[�W��F�B�ȊO�����M���Ȃ��悤�ɂ��܂�</h1><br>
EOM
	if ($ban_hit) {
	print <<"EOM";
���݂̐ݒ�F������<br>
<form action="$script_post" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=limit_do>
<input type=hidden name=bansts value="0">
<input type=submit class=btn value="��������">
</form>
EOM
	} else {
	print <<"EOM";
���݂̐ݒ�F����������<br>
<form action="$script_post" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=limit_do>
<input type=hidden name=bansts value="1">
<input type=submit class=btn value="��������">
</form>
EOM
	}
	print <<"EOM";
<form action="$script_post" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�֋ǂ̍ŏ��̉�ʂ�">
</form>
<form action="$script" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

#------------------#
#  ���ہE�F�B�o�^  #
#------------------#
sub limit_do {

	&chara_load;

	&chara_check;

	# ���ۏ�Ԃ̌Ăяo��
	$lock_file = "$lockfolder/banfr$chara[0].lock";
	&lock($lock_file,'BF');
	open(IN,"$ban_file/$chara[0].cgi");
	@ban_sts = <IN>;
	close(IN);

	@new_ban = "";
	$ban_hit = 0;
	@ban_mes = ('����','�ݒ�');
	foreach (@ban_sts) {
		s/\n//gi;
		s/\r//gi;
		($banid,$bansts) = split(/<>/);
		if ($banid eq "all") {
			if ($in{'bansts'}) {
				push(@new_ban,"all<>\n");
				$ban_hit = 1;
			}
		} else {
			push(@new_ban,"$_");
		}
	}

	if (!$ban_hit && $in{'bansts'}) {
			push(@new_ban,"all<>\n");
	}

	open(OUT,">$ban_file/$chara[0].cgi");
	print OUT @new_ban;
	close(OUT);
	&unlock($lock_file,'BF');

	&header;

	print <<"EOM";
<h1>������$ban_mes[$in{'bansts'}]���܂����B</h1>
<hr size=0>
<form action="$script_post" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�֋ǂ̍ŏ��̉�ʂ�">
</form>
<form action="$script" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

#--------------#
# ���ۃV�X�e�� #
#--------------#
sub ban {

	&chara_load;

	&chara_check;

	# �w�b�_�[�\��
	&header;

	print <<"EOM";
<h1>���Ȑl����̃��b�Z�[�W�����ۂł��܂�</h1>
<table>
<tr>
<form action="$script_post" method="post">
<td class="b2" valign="top">
���O���w�肵�ċ���<br>
<input type="text" name="mesname" size=10>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value=ban_do>
<input type=hidden name=bansts value="1">
<input type=submit class=btn value="����">
</td>
</form>
</tr>
<tr>
<form action="$script_post" method="post">
<td class="b2" valign="top">
���݂̋��ێ҃��X�g<br>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value="ban_do">
<input type=hidden name=bansts value="0">
<select name=mesid size=5>
EOM
	# ���ۏ�Ԃ̌Ăяo��
	open(IN,"$ban_file/$chara[0].cgi");
	@ban_sts = <IN>;
	close(IN);

	$ban_hit = 0;
	foreach (@ban_sts) {
		s/\n//gi;
		s/\r//gi;
		($banid,$bansts,$banname) = split(/<>/);
		if ($bansts eq 1) {
			print << "EOM";
<option value = "$banid">$banname����
EOM
			$ban_hit = 1;
		}
	}

	if (!$ban_hit) {
		print "<option value = \"\">���܂���";
	}
	print <<"EOM";
<input type=submit class=btn value="���ۉ���">
</td>
</form>
</tr>
<tr>
<td class="b2" valign="top">
<br>
<form action="$script_post" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�֋ǂ̍ŏ��̉�ʂ�">
</form>
<form action="$script" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
</td>
</tr></table>
EOM

	&footer;

	exit;
}

#--------------#
# �F�B�V�X�e�� #
#--------------#
sub friend {

	&chara_load;

	&chara_check;

	# �w�b�_�[�\��
	&header;

	print <<"EOM";
<h3>��M�������ł����b�Z�[�W���󂯕t���鑊����w��ł��܂�</h3>
<table>
<tr>
<form action="$script_post" method="post">
<td class="b2" valign="top">
���O���w�肵�ēo�^<br>
<input type="text" name="mesname" size=10>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value=ban_do>
<input type=hidden name=bansts value="2">
<input type=submit class=btn value="�F�B�o�^">
</td>
</form>
</tr>
<tr>
<form action="$script_post" method="post">
<td class="b2" valign="top">
���݂̗F�B���X�g<br>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=bansts value="0">
<input type=hidden name=mode value="ban_do">
<select name=mesid size=5>
EOM
	# �F�B�̌Ăяo��
	open(IN,"$ban_file/$chara[0].cgi");
	@ban_sts = <IN>;
	close(IN);

	$ban_hit = 0;
	foreach (@ban_sts) {
		s/\n//gi;
		s/\r//gi;
		($banid,$bansts,$banname) = split(/<>/);
		if ($bansts eq 2) {
			print << "EOM";
<option value = "$banid">$banname����
EOM
			$ban_hit = 1;
		}
	}

	if (!$ban_hit) {
		print "<option value = \"\">���܂���";
	}
	print <<"EOM";
<input type=submit class=btn value="�F�B����">
</td>
</form>
</tr>
<tr>
<td class="b2" valign="top">
<br>
<form action="$script_post" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�֋ǂ̍ŏ��̉�ʂ�">
</form>
<form action="$script" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
</td>
</tr></table>
EOM

	&footer;

	exit;
}

#------------------#
#  ���ہE�F�B�o�^  #
#------------------#
sub ban_do {

	&chara_load;

	&chara_check;

	if($in{'mesid'} eq "" && $in{'mesname'} eq "") {
		&error("���肪�w�肳��Ă��܂���$back_form");
	}

	&all_data_read;

	$mhit = 0;
	foreach (@RANKING) {
		s/\n//gi;
		s/\r//gi;
		@aite_data = split(/<>/);
		if ($aite_data[0] eq $in{'mesid'} || $aite_data[4] eq $in{'mesname'}) {
			$mhit = 1;
			last;
		}
	}

	if ($aite_data[0] eq $chara[0]) {
		&error("�����͓o�^�ł��܂���I$back_form");
	}

	# ���肪������Ȃ���
	if (!$mhit) {
		&error("���肪������܂���I$back_form");
	}

	# ���ۏ�Ԃ̌Ăяo��
	$lock_file = "$lockfolder/banfr$chara[0].lock";
	&lock($lock_file,'BF');
	open(IN,"$ban_file/$chara[0].cgi");
	@ban_sts = <IN>;
	close(IN);

	@new_ban = "";
	$ban_hit = 0;
	@ban_mes = ('����','���ۓo�^','�F�B�o�^');
	foreach (@ban_sts) {
		s/\n//gi;
		s/\r//gi;
		($banid,$bansts) = split(/<>/);
		if ($banid eq $aite_data[0]) {
			if ($in{'bansts'}) {
				push(@new_ban,"$aite_data[0]<>$in{'bansts'}<>$aite_data[4]<>\n");
			}
			$ban_hit = 1;
		} else {
			push(@new_ban,"$_\n");
		}
	}

	if (!$ban_hit) {
		push(@new_ban,"$aite_data[0]<>$in{'bansts'}<>$aite_data[4]<>\n");
	}

	open(OUT,">$ban_file/$chara[0].cgi");
	print OUT @new_ban;
	close(OUT);
	&unlock($lock_file,'BF');

	&header;

	print <<"EOM";
<h1>$aite_data[4]�����$ban_mes[$in{'bansts'}]���܂����B</h1>
<hr size=0>
<form action="$script_post" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�֋ǂ̍ŏ��̉�ʂ�">
</form>
<form action="$script" method="post">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

