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
#     http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi 		#
#---------------------------------------------------------------#
# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �퓬���C�u�����̓ǂݍ���
require 'battle.pl';
# �`�����v��p���C�u�����ǂݍ���
require 'wbattle.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# ���̃t�@�C���p�ݒ�
$backgif = $tennka_back;
$midi = $tennka_midi;

#================================================================#
#����������������������������������������������������������������#
#�� �����艺��CGI�Ɏ��M�̂�����ȊO�͈���Ȃ��ق�������ł��@��#
#����������������������������������������������������������������#
#================================================================#

#--------------#
#�@���C�������@#
#--------------#
if($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}

if ($mode) { &$mode; }

&log_in;

exit;

#------------#
#  ��t���  #
#------------#
sub log_in{

	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/tim.lock";
	&lock($lock_file,'TM');
	open(IN,"$all_data_time");
	@all_time = <IN>;
	close(IN);

	$hit=0;
	foreach(@all_time){
		($rankmode,$ranktime) = split(/<>/);
		if ($rankmode eq "tenka") { $hit=1;last; }
	}

	$ltime = time();
	$btime = $ltime - $ranktime;
	$ztime = int($btime/3600);

	if ($btime > 3600*24 || !$hit) {

		$hit=0;
		@item_new=();
		foreach (@all_time) {
			($rankmode,$ranktime) = split(/<>/);
			if ($rankmode eq "tenka") {
				unshift(@item_new,"tenka<>$ltime<>\n");
				$hit=1;
			} else {
				push(@item_new,"$_");
			}
		}

		if (!$hit) { unshift(@item_new,"tenka<>$ltime<>\n"); }

		open(OUT,">$all_data_time");
		print OUT @item_new;
		close(OUT);
		$lock_file = "$lockfolder/tim.lock";
		&unlock($lock_file,'TM');

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

		$tenka_hit = 0;
		$tenka_ninzu = @temp_member;
		if ($tenka_su > $tenka_ninzu) {
			$tenka_su = $tenka_ninzu;
			$tenka_hit = 1;
		}
		# �z��19�ԖڂŃ\�[�g
		@tmp = map {(split /<>/)[18]} @temp_member;
		@RANKING = @temp_member[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

		for ($si=0;$si<$tenka_su;$si++) {
			push(@tenka_member,"$RANKING[$si]");
		}

		open(OUT,">$all_tenka");
		print OUT @tenka_member;
		close(OUT);

	} else {
		$lock_file = "$lockfolder/tim.lock";
		&unlock($lock_file,'TM');

		open(IN,"$all_tenka");
		@tenka_member = <IN>;
		close(IN);

		$tenka_hit = 0;
		$tenka_ninzu = @tenka_member;
		if ($tenka_su > $tenka_ninzu) {
			$tenka_hit = 1;
		}
	}

	open(IN,"$tenka_log");
	@tenka_log = <IN>;
	close(IN);

	&header;

	print << "EOM";
<h1>�V���ꕐ����</h1>
<hr size=0>
<FONT SIZE=3>
<B>�i���</B><BR>
�u
�悤�����I�V���ꕐ����ցI<br>
�����͂���$main_title�ł̍ŋ��̃v���C���[���������������Ă�������ƂȂ��Ă��܂��I<br>
���Ȃ���$chara[4]����ł��ˁI<br>
���킵�Ă݂܂����H
�v
<table width = "80%">
<tr>
<td width = "50%" align = "left" valign = "top">
<table width = "95%">
<tr>
<td align="center" id="td2" class="b2" colspan = "2">
�V���ꕐ������o�[���X�g($ztime���ԑO�X�V)
</td>
</tr>
<tr>
<td align="right" class="b2">
���O
</td>
<td align="right" class="b2">
���x��
</td>
</tr>
EOM

	foreach (@tenka_member) {
		s/\n//gi;
		s/\r//gi;
		@tenka = split(/<>/);
		print << "EOM";
<tr>
<td align="right" class="b2">
$tenka[4]
</td>
<td align="right" class="b2">
$tenka[18]
</td>
</tr>
EOM
	}

	print << "EOM";
</table>
</td>
<td width = "50%" align = "left" valign = "top">
<table width = "95%">
<tr>
<td align="center" id="td2" class="b2" colspan = "3">
�����ŋ߂̐��e��
</td>
</tr>
<tr>
<td align="right" class="b2">
���O
</td>
<td align="right" class="b2">
���x��
</td>
<td align="right" class="b2">
����
</td>
</tr>
EOM

	if (@tenka_log) {
		foreach (@tenka_log) {
			s/\n//gi;
			s/\r//gi;
			@tenka = split(/<>/);
			print << "EOM";
<tr>
<td align="right" class="b2">
<a href="$scripta?mode=chara_sts&id=$tenka[0]">$tenka[1]</a>
</td>
<td align="right" class="b2">
$tenka[2]
</td>
<td align="right" class="b2">
$tenka[3]
</td>
</tr>
EOM
		}
	} else {
			print << "EOM";
<tr>
<td align="center" class="b2" colspan ="2">
���̂悤�ȖҎ҂͂܂����܂���
</td>
</tr>
EOM
	}
	print << "EOM";
</table>
</td></tr></table>
EOM
	if ($chara[28] != $boss) {
		print '��x�A�`�����v�ɒ��킵�ĉ�����';
	} elsif (!$tenka_hit) {
		print << "EOM";
<form action="$script_tenka" method="POST">
<input type="hidden" name="mode" value="battle">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="hidden" name="no" value="1">
<input type="submit" class="btn" value="�V���ꕐ����ɒ��킷��">
</form>
EOM
	} else {
		print "�l��������܂���";
	}
	print << "EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;

}

#------------#
#  �퓬���  #
#------------#
sub battle {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$ltime = time();
	$ltime = $ltime - $chara[27];
	$ztime = $b_time - $ltime;

	if ($ztime > 0) {
		&tenka_error;
	}

	open(IN,"$all_tenka");
	@tenka_member = <IN>;
	close(IN);

	$aite = $tenka_su + $chara[28] - $boss - 1;

	if ($in{'no'} != $tenka_su - $aite) {
		&error("�L�����f�[�^�s����");
	}

	@winner_data = split(/<>/,$tenka_member[$aite]);

	&winner_data;

	# �܋��̌���
	$gold = int(rand($syoukin)+1) * int($winner[17]);

	&item_load;

	&acs_add;

	&wacs_add;

	$khp_flg = $chara[15];
	$whp_flg = $winner[15];

	$i=1;$j=0;@battle_date=();
	foreach (1..$turn) {

		&shokika;

		&tyousensya;
		&winner_atack;

		&tyosenwaza;
		&winwaza;

		&acs_waza;
		&wacs_waza;

		&battle_clt;
		&battle_kaihi;

		&battle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	&sentoukeka;
	$chara[25] = $sentou_limit;
	$chara[28]--;

	&acs_sub;
	&wacs_sub;

	&levelup;

	$chara[15] = $khp_flg + int(rand($chara[10]));
	if($chara[15] > $chara[16]) { $chara[15] = $chara[16]; }
	$winner[15] = $whp_flg + int(rand($winner[9]));
	if($winner[15] > $winner[16]) { $winner[15] = $winner[16]; }
	if($chara[15] <= 0) { $chara[15] = 1; }
	if($winner[15] <= 0) { $winner[15] = 1; }
	$chara[19] += $gold;
	if($chara[19] < 0){$chara[19] = 0;}
	if($chara[19] > $gold_max){$chara[19] = $gold_max;}

	if($chara[15] == 1) { $chara[15] = $chara[16]; }

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$next_winner = $chara[28] + $tenka_su - $boss;

	# ������e
	if ($win == 1 && $next_winner == 0) {
		&get_time($chara[27]);

		&all_message("$chara[4]���񂪓V���ꕐ����𐧔e����܂����I");

		$lock_file = "$lockfolder/tnk.lock";
		&lock($lock_file,'TENKA');
		open(IN,"$tenka_log");
		@tenka_log = <IN>;
		close(IN);
		$log_num =@tenka_log;
		if ($tenaka_su < $log_num) {
			pop(@tenka_log);
		}

		unshift(@tenka_log,"$chara[0]<>$chara[4]<>$chara[18]<>$gettime<>\n");
		open(OUT,">$tenka_log");
		print OUT @tenka_log;
		close(OUT);
		&unlock($lock_file,'TENKA');
	}

	&header;

	$juni = $tenka_su - $in{'no'} + 1;

		print << "EOM";
<font class=yellow size=5>�V���ꕐ����@��<font class=red>$in{'no'}</font>���I�I</font><br>
�����x�����$tenka_su�l�̂�����$juni�ʂ̃L�����N�^�[�Ƃ̐퓬<br>
<h1>$chara[4]�́A$winner[3]�ɐ킢�𒧂񂾁I�I</h1>
<hr size=0><br>
EOM
	$in{'no'}++;
	$i=0;
	foreach(@battle_date){
		print "$battle_date[$i]";
		$i++;
	}
	
	if ($win) {
		if ($next_winner != 0) {
			print << "EOM";
$comment<br>$chara[4]�́A<b>$exp</b>�̌o���l����ɓ��ꂽ�B$winner[3]�̏܋�<b>$gold</b>G��ɓ��ꂽ�B<br>
<form action="$script_tenka" method="POST">
<input type="hidden" name="mode" value="battle">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="hidden" name="no" value="$in{'no'}">
<input type="submit" class="btn" value="���̐킢��">
</form>
EOM
		} else {
		print "<font class=yellow>$comment<br>$chara[4]�́A�V���ꕐ����ŗD�������I�I</font><b>$exp</b>�̌o���l����ɓ��ꂽ�B�D���܋�<b>$gold</b>G��ɓ��ꂽ�B<br>\n";
		}
	} else {
		print "$comment<br>$chara[4]�́A<b>$exp</b>�̌o���l����ɓ��ꂽ�B�����������ɂȂ����E�E�E(��)<br>\n";
	}

	$new_chara =~ s/</&lt;/g;
	$new_chara =~ s/>/&gt;/g;

	print << "EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

#----------------#
#  �҂����ԕ\��  #
#----------------#
sub tenka_error {

	foreach (keys %lock_flg) {
		if ($lock_flg{$_}) {
			if ($lockkey == 3) {
				foreach (@flock) {
					($flock_pre,$flock_file) = split(/,/);
					if ($flock_file eq $_) {
						last;
					}
				}
			}
			&unlock($_,$flock_pre);
		}
	}

	&header;

	&time_view;

       print <<"EOM";
<center><hr width=400>
<font color=red><B>�܂��퓬�ł��܂���I</B></font><br>
<FORM NAME="form1">
����<INPUT TYPE="text" NAME="clock" SIZE="3">�b�҂��ĉ�����
</FORM>
<form action="$script_tenka" method="POST">
<input type="hidden" name="mode" value="battle">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type="hidden" name="no" value="$in{'no'}">
<input type="submit" class="btn" value="���̐킢��">
</form>
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
<hr width=400>
</center>
EOM

	&footer;

	exit;

}
