#!/usr/local/bin/perl

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
#�@http://www.eriicu.com
#�@icu@kcc.zaq.ne.jp
#------------------------------------------------------#
#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p���� #
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B     	#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B   	#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi             #
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B   	#
#---------------------------------------------------------------#
# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �A�C�e�����C�u�����̓ǂݍ���
require 'item.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# ���̃t�@�C���p�ݒ�
$backgif = $shop_back;
$midi = $shop_midi;

# [�ݒ�͂����܂�]------------------------------------------------------------#

# �����艺�́ACGI�̂킩����ȊO�́A�ύX���Ȃ��ق����ǂ��ł��B

#-----------------------------------------------------------------------------#
if($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="$def_shop" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="�߂�">
</form>
EOM

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}
if($mode) { &$mode; }

&item_view;

exit;

#----------------#
#  �A�C�e���\��  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	open(IN,"$def_file");
	@log_item = <IN>;
	close(IN);

	$hit=0;
	foreach(@log_item){
		($si_no,$si_name,$si_dmg,$si_gold) = split(/<>/);
		if($chara[29] eq "$si_no"){ $hit=1;last; }
	}

	if(!$hit) {
		$si_name="���i��";
		$si_dmg="0";
		$si_gold="0";
	}

	$ui_gold = int($si_gold / 3) * 2;


	open(IN,"$def_folder/def$chara[14].ini");
	@item_array = <IN>;
	close(IN);

	&header;

	print <<"EOM";
<h1>�h�</h1>
<hr size=0>

<FONT SIZE=3>
<B>�h��̃}�X�^�[</B><BR>
�u��������Ⴂ�I�����h����Ă��`�B���̑嗤�̒�����A��������Ԃ̕i��������I<BR>
�@���A�Ȃ񂾂��A<B>$chara[4]</B>����Ȃ����B���C�ɂ��Ă������H
<BR>����$chara_syoku[$chara[14]]������Ă�̂��B
<BR>���$chara_syoku[$chara[14]]�p�̖h�����ׂ����񂾂�I
<BR>
�@�܂��A������茩�Ă����Ă���B
<BR><BR>���������I�ŋߑ����i�̉������͂��߂��񂾁B�v
</FONT>
<br><hr>���݂̏������F$chara[19] �f<br>
<table>
<tr>
<th></th><th>No.</th><th>�Ȃ܂�</th><th>�З�</th><th>���i</th></tr>
<tr>
<form action="$def_shop" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_sell>
EOM
if ($hit) { print "<input type=submit class=btn value=\"����\">"; }
	print <<"EOM";
</th></form><th>���݂̑����i</th><th>$si_name</th><th>$si_dmg</th><th>$ui_gold</th></tr></table>
<form action="$def_shop" method="post">
<table>
EOM

	foreach (@item_array) {
		($ino,$iname,$idmg,$igold) = split(/<>/);
		print "<tr><td class=b1 align=\"center\">\n";
		if ($chara[19] >= $igold) {
			print "<input type=radio name=item_no value=\"$ino\">";
		} else {
			print "�~";
		}
		print "</td><td align=right class=b1>$ino</td><td class=b1>$iname</td><td align=right class=b1>$idmg</td><td align=right class=b1>$igold</td>\n";
		print "</tr>\n";
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=submit class=btn value="�h��𔃂�">
</form>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub item_buy {
	

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"$def_folder/def$chara[14].ini");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($d_no,$d_name,$d_dmg,$d_gold,$d_hit) = split(/<>/);
		if($in{'item_no'} eq "$d_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	if($chara[19] < $d_gold) { &error("����������܂���$back_form"); }
	else { $chara[19] = $chara[19] - $d_gold; }

	$chara[26] = $host;

	$lock_file = "$lockfolder/sdefe$in{'id'}.lock";
	&lock($lock_file,'SD');
	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item_num = @souko_item;

	if ($souko_item_num >= $def_max) {
		&error("�h��q�ɂ������ς��ł��I$back_form");
	}

	push(@souko_item,"$d_no<>$d_name<>$d_dmg<>$d_gold<>$d_hit<>\n");

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);
	&unlock($lock_file,'SD');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�h��̃}�X�^�[</B><BR>
�u���x����`�I<br>
�������h��͂��񂽂̖h��q�ɂɑ����Ă�������I
�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub item_sell {
	

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$chara[26] = $host;

	open(IN,"$def_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold) = split(/<>/);
		if($chara[29] eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }
	if(!$chara[29]) { &error("����ȃA�C�e���͑��݂��܂���"); }
	$ui_gold = int($i_gold / 3) * 2;

	$chara[19] = $chara[19] + $ui_gold;
	if($chara[19] > $gold_max){$chara[19] = $gold_max;}

	$chara[29] = 0;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	&def_lose;

	&item_regist;
	&unlock($lock_file,'IM');

	&header;

	print <<"EOM";
<h1>$i_name�𔄂�܂���</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
