#!/usr/local/bin/perl --

#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠��T.CUMRO����ɂ���܂��B
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
#�@http://www.eriicu.com
#�@icu@kcc.zaq.ne.jp
#------------------------------------------------------#

#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
# 3. �ݒu������F����Ɋy����ł��炤�ׂɂ��AWeb�����O�ւ��ЎQ��#
#    ���Ă�������m(__)m						#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi�@�@�@�@�@�@�@�@�@�@�@#
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �A�C�e�����C�u�����̓ǂݍ���
require 'item.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# ������Ԃ̐ݒ�(������Ԃŏ������Ă��镐��E�h��B0�́u�Ȃ��v�ɂȂ�܂�)
$first_item = 0;	# ����NO
$first_def = 0;		# �h��NO
$first_acs = 0;		# �����iNO

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
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
	}

if($mode) { &$mode; }

&chara_make;

#----------------------#
#  �L�����N�^�쐬���  #
#----------------------#
sub chara_make {

	if($chara_stop){
		&error("���݃L�����N�^�[�̍쐬�o�^�͂ł��܂���"); 
	}

	# �w�b�_�[�\��
	&header;

	print <<"EOM";
<h1>�L�����N�^�쐬���</h1>
<hr size=0>
<form action="$chara_make" method="post">
<input type="hidden" name="mode" value="make_pre">
<table border=1>
<tr>
<td class="b1" colspan="2">
�E�L�����N�^�[�̓o�^��<b>��l�P�L����</b>�ł��肢���܂��B��l�ȏ�o�^����Ă��邱�Ƃ����������ꍇ�́A<b>�x�������폜</b>�����Ă��������܂��B<br>
�E�����点���b�Z�[�W��A�s���s�ׂ����o�����ꍇ�́A<b>�x���Ȃ��L�����N�^�[���폜</b>�����Ă��������܂��B<br>
�E�����������O�̕����͂��܂���B�L���̋���ł܂߂Ƀo�b�N�A�b�v���Ƃ��Ă����Ă��������B<br>
�E�X�V�{�^���A�ł�A�����̃E�C���h�E�ł̃v���C�A�e��<b>�{�^���A�ł̓L�������O�����̌���</b>�ƂȂ�܂��̂�<b>��΂Ɏ~�߂Ă��������B</b><br>
�E�T�[�o�[�̕��ׂ��傫���Ȃ�ƁA�T�[�o�[�Ǘ��҂ɍ폜����Ă��܂���������Ȃ��̂ŁA�X�V�{�^���A�ł�<b>��΂Ɏ~�߂Ă��������B</b><br>
�E�{�Q�[�����v���C���Ẵg���u���E���Q�ȂǂɊւ��܂��ẮA<b>�Ǘ��҂͈�؂̐ӔC�𕉂��܂���B</b><br>
�ȏ��ǂ��������̏�œo�^���Ă��������B</font>
</td>
</tr>
<tr>
<td class="b1">ID</td>
<td>
<input type="text" name="id" size="10" value="$in{'id'}"><br>
�����D���Ȕ��p�p������4�`8�����ȓ��ł��L�����������B
</td>
</tr>
<tr>
<td class="b1">�p�X���[�h</td>
<td>
<input type="password" name="pass" size="10" value="$in{'pass'}"><br>
�����D���Ȕ��p�p������4�`8�����ȓ��ł��L�����������B
</td>
</tr>
<tr>
<td class="b1">�p�X���[�h�ύX�p�P��</td>
<td>
<input type="text" name="passchange" size="10" value="$in{'passchange'}"><br>
���p�X���[�h��ύX���鎞�̃p�X���[�h�ł��B���Ȃ�d�v�Ȃ̂ŖY��Ȃ��悤�Ƀ��������悤�ɂ��肢���܂��B
</td>
</tr>
<tr>
<td class="b1">�z�[���y�[�W��</td>
<td>
<input type="text" name="site" size="40" value="$in{'site'}"><br>
�����Ȃ��̃z�[���y�[�W�̖��O����͂��Ă��������B�i�Ȃ��ꍇ�̓I�X�X���g�o�j
</td>
</tr>
<tr>
<td class="b1">URL</td>
<td>
<input type="text" name="url" size="50" value="$in{'url'}"><br>
�����Ȃ��̃z�[���y�[�W�̃A�h���X���L�����Ă��������B�i�Ȃ��ꍇ�̓I�X�X���g�o�j
</td>
</tr>
<tr>
<td class="b1">�L�����N�^�[�̖��O</td>
<td>
<input type="text" name="c_name" size="30" value="$in{'c_name'}"><br>
���쐬����L�����N�^�[�̖��O����͂��Ă��������B
</td>
</tr>
<tr>
<td class="b1">�L�����N�^�[�̐���</td>
<td>
<input type="radio" name="sex" value="0">���@
<input type="radio" name="sex" value="1" checked>�j<br>
���쐬����L�����N�^�[�̐��ʂ�I�����Ă��������B
</td>
</tr>
<tr>
<td class="b1">�L�����N�^�[�̃C���[�W</td>
<td><input type="text" name="chara" size="10" value="$in{'chara'}">
<br>
���쐬����L�����N�^�[�̉摜�ԍ����w�肵�Ă��������B
(<a href="$img_all_list" target="_blank">$vote_gazou</a>)
<br>
�w�肵�Ȃ�������A�Ȃ��ԍ������Ă�����ƃ����_���őI�΂�܂��B
</td>
</tr>
<tr>
<td class="b1">�L�����N�^�[�̏����E��</td>
<td>
<select name="syoku">
<option value="0">$chara_syoku[0]</option>
<option value="1">$chara_syoku[1]</option>
<option value="2">$chara_syoku[2]</option>
<option value="3">$chara_syoku[3]</option>
</select>
</td>
</tr>
<tr>
<td colspan="2" align="center">
<input type="submit" class="btn" value="����œo�^">
</td>
</tr>
</table>
</form>
EOM
	# �t�b�^�[�\��
	&footer;

	exit;
}

#----------------#
#  �o�^�m�F���  #
#----------------#
sub make_pre {

	if ($in{'id'} =~ m/[^0-9a-zA-Z]/){
		&make_error("ID�ɔ��p�p�����ȊO�̕������܂܂�Ă��܂��B"); 
	}
	elsif ($in{'pass'} =~ m/[^0-9a-zA-Z]/){
		&make_error("�p�X���[�h�ɔ��p�p�����ȊO�̕������܂܂�Ă��܂��B"); 
	}
	elsif ($in{'id'} eq "" or length($in{'id'}) < 4 or length($in{'id'}) > 8) {
		&make_error("ID�́A4�����ȏ�A8�����ȉ��œ��͂��ĉ������B");
	}
	elsif ($in{'pass'} eq "" or length($in{'pass'}) < 4 or length($in{'pass'}) > 8) {
		&make_error("�p�X���[�h�́A4�����ȏ�A8�����ȉ��œ��͂��ĉ������B"); 
	}
	elsif ($in{'c_name'} eq "") {
		&make_error("�L�����N�^�[�̖��O�����L���ł�"); 
	}
	elsif ($in{'sex'} eq "") {
		&make_error("���ʂ��I������Ă��܂���");
	}
	elsif ($in{'syoku'} < 0 || $in{'syoku'} > 4) {
		&make_error("�E�Ƃ��I������Ă��܂���");
	}
	elsif($in{'passchange'} eq "") {
		&make_error("�p�X���[�h�ύX�p�P�ꂪ�ݒ肳��Ă��܂���");
	}

	if ($name_ban) {
		open(IN,"$all_data_file");
		@all_data = <IN>;
		close(IN);
		foreach (@all_data) {
			@all_chara = split(/<>/);
			if ($all_chara[4] eq $in{'c_name'}) {
				close(IN);
				&make_error("���ꖼ�̃L�����N�^�[�����܂�");
			}
		}
	}

	if (-e "./charalog/$in{'id'}.cgi") {
		&make_error("����ID�͂��łɎg�p����Ă��܂�");
	}

	$img_sum = @chara_img;
	if (($in{'chara'} ne 0 && !$in{'chara'}) || $in{'chara'} < 0 || $in{'chara'} > $img_sum){
		$in{'chara'} = int(rand($img_sum));
	}

	if ($in{'site'} eq "") {
		$in{'site'} = '�����̂b�f�h�̂g�o';
	}
	if ($in{'url'} eq "") {
		$in{'url'} = 'http://www.eriicu.com';
	}

		if($in{'sex'}) { $esex = "�j"; } else { $esex = "��"; }
		$next_ex = $lv_up;

		&header;

		print <<"EOM";
<h1>�o�^�m�F���</h1>
�ȉ��̓��e�ł�낵���ł��傤���H
<hr size=0>

<table border=1>
<tr>
<td class="b1">�z�[���y�[�W</td>
<td colspan="4"><a href="http\:\/\/$in{'url'}">$in{'site'}</a></td>
</tr>
<tr>
<td rowspan="8" align="center"><img src="$img_path/$chara_img[$in{'chara'}]"></td>
<td class="b1">�Ȃ܂�</td>
<td>$in{'c_name'}</td>
<td class="b1">����</td>
<td>$esex</td>
</tr>
<tr>
<td class="b1">�E��</td>
<td>$chara_syoku[$in{'syoku'}]</td>
<td class="b1">����</td>
<td>$intgold</td>
</tr>
<tr>
<td class="b1">���x��</td>
<td>1</td>
<td class="b1">�o���l</td>
<td>0/$next_ex</td>
</tr>
<tr>
<td class="b1">�p�X���[�h�ύX�p�P��</td>
<td><font color="red" size += "2"><b>$in{'passchange'}</b></font></td>
<td class="b1" colspan="2"><b>���d�v�Ȃ̂ŕK���������ĉ�������</b></td>
</tr>
</table>
<form action="$chara_make" method="post">
<input type=hidden name="mode" value="make_end">
<input type=hidden name="id" value="$in{'id'}">
<input type=hidden name="pass" value="$in{'pass'}">
<input type=hidden name="passchange" value="$in{'passchange'}">
<input type=hidden name="site" value="$in{'site'}">
<input type=hidden name="url" value="$in{'url'}">
<input type=hidden name="c_name" value="$in{'c_name'}">
<input type=hidden name="sex" value="$in{'sex'}">
<input type=hidden name="chara" value="$in{'chara'}">
<input type=hidden name="syoku" value="$in{'syoku'}">
<input type=submit class="btn" value="�쐬����"></form>
<form action="$chara_make" method="post">
<input type=hidden name="id" value="$in{'id'}">
<input type=hidden name="pass" value="$in{'pass'}">
<input type=hidden name="passchange" value="$in{'passchange'}">
<input type=hidden name="site" value="$in{'site'}">
<input type=hidden name="url" value="$in{'url'}">
<input type=hidden name="c_name" value="$in{'c_name'}">
<input type=hidden name="sex" value="$in{'sex'}">
<input type=hidden name="chara" value="$in{'chara'}">
<input type=hidden name="syoku" value="$in{'syoku'}">
<input type=submit class="btn" value="�߂�"></form>
EOM

		&footer;

		exit;
}

#----------------#
#  �o�^�������  #
#----------------#
sub make_end {

	&get_host;

	if($chara_stop){ &error("���݃L�����N�^�[�̍쐬�o�^�͂ł��܂���"); }

	if ($in{'id'} =~ m/[^0-9a-zA-Z]/){
		&make_error("ID�ɔ��p�p�����ȊO�̕������܂܂�Ă��܂��B"); 
	}
	elsif ($in{'pass'} =~ m/[^0-9a-zA-Z]/){
		&make_error("�p�X���[�h�ɔ��p�p�����ȊO�̕������܂܂�Ă��܂��B"); 
	}
	elsif ($in{'id'} eq "" or length($in{'id'}) < 4 or length($in{'id'}) > 8) {
		&make_error("ID�́A4�����ȏ�A8�����ȉ��œ��͂��ĉ������B");
	}
	elsif ($in{'pass'} eq "" or length($in{'pass'}) < 4 or length($in{'pass'}) > 8) {
		&make_error("�p�X���[�h�́A4�����ȏ�A8�����ȉ��œ��͂��ĉ������B"); 
	}
	elsif ($in{'c_name'} eq "") {
		&make_error("�L�����N�^�[�̖��O�����L���ł�"); 
	}
	elsif($in{'sex'} eq "") {
		&make_error("���ʂ��I������Ă��܂���");
	}
	elsif($in{'passchange'} eq "") {
		&make_error("�p�X���[�h�ύX�p�P�ꂪ�ݒ肳��Ă��܂���");
	}
	elsif($in{'syoku'} eq "") {
		&make_error("�E�Ƃ��I������Ă��܂���");
	}
	if($in{'site'} eq "") {
		$in{'site'} = '�����̂b�f�h�̂g�o';
	}
	if($in{'url'} eq "") {
		$in{'url'} = 'http://www.eriicu.com';
	}

	if ($name_ban && $ip_ban) {
		open(IN,"$all_data_file");
		@all_data = <IN>;
		close(IN);
		foreach (@all_data) {
			@all_chara = split(/<>/);
			if ($all_chara[4] eq $in{'c_name'}) {
				close(IN);
				&make_error("���ꖼ�̃L�����N�^�[�����܂�");
			}
			elsif ($all_chara[26] eq $host && $all_chara[0] ne 'test') {
				close(IN);
				&error("����h�o����o�^���ꂽ�L���������łɑ��݂��܂��B");
			}
		}
	}
	elsif ($ip_ban) {
		open(IN,"$all_data_file");
		@all_data = <IN>;
		close(IN);
		foreach (@all_data) {
			@all_chara = split(/<>/);
			if ($all_chara[26] eq $host && $all_chara[0] ne 'test') {
				close(IN);
				&error("����h�o����o�^���ꂽ�L���������łɑ��݂��܂��B");
			}
		}
	}
	elsif ($name_ban) {
		open(IN,"$all_data_file");
		@all_data = <IN>;
		close(IN);
		foreach (@all_data) {
			@all_chara = split(/<>/);
			if ($all_chara[4] eq $in{'c_name'}) {
				close(IN);
				&make_error("���ꖼ�̃L�����N�^�[�����܂�");
			}
		}
	}

	if (-e "./charalog/$in{'id'}.cgi") {
		&make_error("����ID�͂��łɎg�p����Ă��܂�");
	}

	$img_sum = @chara_img;
	if (($in{'chara'} ne 0 && !$in{'chara'}) || $in{'chara'} < 0 || $in{'chara'} > $img_sum){
		$in{'chara'} = int(rand($img_sum));
	}

	if ($in{'syoku'} == 1) {
		$n_0 = 9;
		$n_1 = 14;
		$n_2 = 10;
		$n_3 = 9;
		$n_4 = 11;
		$n_5 = 8;
		$n_6 = 10;
		$lp = 5;
	} elsif ($in{'syoku'} == 2) {
		$n_0 = 9;
		$n_1 = 10;
		$n_2 = 12;
		$n_3 = 9;
		$n_4 = 11;
		$n_5 = 8;
		$n_6 = 12;
		$lp = 5;
	} elsif ($in{'syoku'} == 3) {
		$n_0 = 11;
		$n_1 = 8;
		$n_2 = 8;
		$n_3 = 11;
		$n_4 = 13;
		$n_5 = 8;
		$n_6 = 12;
		$lp = 5;
	} else {
@kiso_nouryoku = ("9","8","8","9","9","8","8");
		$n_0 = 13;
		$n_1 = 8;
		$n_2 = 8;
		$n_3 = 13;
		$n_4 = 11;
		$n_5 = 10;
		$n_6 = 8;
		$lp = 5;
	}

	$newdata = time();

	$new_chara = "$in{'id'}<>$in{'pass'}<>$in{'site'}<>$in{'url'}<>$in{'c_name'}<>$in{'sex'}<>$in{'chara'}<>$n_0<>$n_1<>$n_2<>$n_3<>$n_4<>$n_5<>$n_6<>$in{'syoku'}<>$kiso_hp<>$kiso_hp<>0<>1<>$intgold<>$lp<>0<>0<>$clt_comment<>$first_item<>$sentou_limit<>$host<>$newdata<>$boss<>$first_def<>0<>$first_acs<>0<>1<>";

	if ($first_item) {
		&item_read($first_item);
	} else {
		&item_lose;
	}

	if ($first_def) {
		&def_read($first_def);
	} else {
		&def_lose;
	}

	if ($first_acs) {
		&acs_read($first_acs);
	} else {
		&acs_lose;
	}

	foreach(@item){
		$new_item .="$_<>";
	}

	$lock_file = "$lockfolder/all.lock";
	&lock($lock_file,'ALL');
	open(OUT,">>./$all_data_file"); 
	print OUT "$new_chara\n"; 
	close(OUT); 
	&unlock($lock_file,'ALL');

	open(OUT,">./charalog/$in{'id'}.cgi"); 
	print OUT $new_chara; 
	close(OUT); 

	open(OUT,">./$pass_folder/$in{'id'}.cgi"); 
	print OUT "$in{'pass'}<>$in{'passchange'}<>$newdata<>$host<>\n"; 
	close(OUT); 

	open(OUT,">./item/$in{'id'}.cgi"); 
	print OUT $new_item; 
	close(OUT);

	if($in{'sex'}) { $esex = "�j"; } else { $esex = "��"; }
	$next_ex = $lv * $lv_up;

	&all_message("$in{'c_name'}���񂪐V���ɃL�����쐬����܂����I�݂Ȃ����낵���I");

		&header;

		print <<"EOM";
<h1>�o�^�������</h1>
�ȉ��̓��e�œo�^���������܂����B
<hr size=0>
<table border=1>
<tr>
<td class="b1">�z�[���y�[�W</td>
<td colspan="4"><a href="http\:\/\/$in{'url'}">$in{'site'}</a></td>
</tr>
<tr>
<td rowspan="8" align="center"><img src="$img_path/$chara_img[$in{'chara'}]"></td>
<td class="b1">�Ȃ܂�</td>
<td>$in{'c_name'}</td>
<td class="b1">����</td>
<td>$esex</td>
</tr>
<tr>
<td class="b1">�E��</td>
<td>$chara_syoku[$in{'syoku'}]</td>
<td class="b1">����</td>
<td>$intgold</td>
</tr>
<tr>
<td class="b1">���x��</td>
<td>1</td>
<td class="b1">�o���l</td>
<td>0/$next_ex</td>
</tr>
<tr>
<td class="b1">HP</td>
<td>$kiso_hp</td>
<td class="b1"></td>
<td></td>
</tr>
<tr>
<td class="b1">��</td>
<td>$n_0</td>
<td class="b1">����</td>
<td>$n_1</td>
</tr>
<tr>
<td class="b1">�M�S</td>
<td>$n_2</td>
<td class="b1">������</td>
<td>$n_3</td>
</tr>
<tr>
<td class="b1">��p��</td>
<td>$n_4</td>
<td class="b1">����</td>
<td>$n_5</td>
</tr>
<tr>
<td class="b1">����</td>
<td>$n_6</td>
<td class="b1">�J���}</td>
<td>$lp</td>
</tr>
</table>
<form action="$loginscript" method="post">
<input type="hidden" name=mode value=log_in>
<input type="hidden" name=id value="$in{'id'}">
<input type="hidden" name=pass value="$in{'pass'}">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM

		&footer;

		exit;
}

#--------------------#
#  �o�^�p�G���[���  #
#--------------------#
sub make_error{
	&header;
	print "<center><hr width=400><h3>ERROR !</h3>\n";
	print "<font color=red><B>$_[0]</B></font>\n";
	print "<hr width=400></center>\n";
	print <<"EOM";
<br>
<form action="$chara_make" method="post">
<input type=hidden name="id" value="$in{'id'}">
<input type=hidden name="pass" value="$in{'pass'}">
<input type=hidden name="passchange" value="$in{'passchange'}">
<input type=hidden name="site" value="$in{'site'}">
<input type=hidden name="url" value="$in{'url'}">
<input type=hidden name="c_name" value="$in{'c_name'}">
<input type=hidden name="sex" value="$in{'sex'}">
<input type=hidden name="chara" value="$in{'chara'}">
<input type=hidden name="syoku" value="$in{'syoku'}">
<input type=submit class="btn" value="�߂�"></form>
EOM
	print "<a href=\"$scripto\">TOP�y�[�W��</a>\n";
	print "</body></html>\n";
	exit;
}