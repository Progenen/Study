"use client";

import React, { useState } from "react";
import { FFmpeg } from "@ffmpeg/ffmpeg";
import { fetchFile } from "@ffmpeg/util";
import Modal from "./Modal";

interface AudioCutterModalProps {
  isOpen: boolean;
  onClose: (open: boolean) => void;
  song: any; // Определите тип объекта песни, если известно
  songUrl: string;
}

const AudioCutterModal: React.FC<AudioCutterModalProps> = ({ isOpen, onClose, song, songUrl }) => {
  const [startTime, setStartTime] = useState<number>(0);
  const [endTime, setEndTime] = useState<number>(10); // По умолчанию обрезка на первых 10 сек.
  const [isProcessing, setIsProcessing] = useState<boolean>(false);
  const [downloadLink, setDownloadLink] = useState<string | null>(null);

  const handleCut = async () => {
    if (endTime <= startTime) {
      alert("Конечное время должно быть больше начального.");
      return;
    }

    setIsProcessing(true);

    try {
      const ffmpeg = new FFmpeg();
      await ffmpeg.load();

      // Загружаем файл
      const response = await fetch(songUrl);
      const audioData = await response.blob();

      // Записываем файл во временное хранилище
      const fileName = "input.mp3";
      const outputFileName = "output.mp3";
      ffmpeg.writeFile(fileName, await fetchFile(audioData));

      // Выполняем обрезку
      await ffmpeg.exec([
        "-i",
        fileName,
        "-ss",
        startTime.toString(),
        "-to",
        endTime.toString(),
        "-c",
        "copy",
        outputFileName
      ]);

      // Получаем результат
      const data = await ffmpeg.readFile(outputFileName);
      console.log(data);
      const blob = new Blob([data], { type: "audio/mpeg" }); // Теперь это правильный Uint8Array

      const url = URL.createObjectURL(blob);
      // Устанавливаем ссылку для скачивания
      setDownloadLink(url);

      // Освобождаем память
      ffmpeg.deleteFile(fileName);
      ffmpeg.deleteFile(outputFileName);
    } catch (error) {
      console.error("Ошибка обрезки аудио:", error);
      alert("Не удалось обрезать аудио.");
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <Modal
      isOpen={isOpen}
      onChange={onClose}
      title={`Редактирование: ${song.title}`}
      description="Укажите начальное и конечное время для вырезания фрагмента."
    >
      <div className="flex flex-col gap-4">
        <audio controls className="w-full">
          <source src={songUrl} type="audio/mpeg" />
          Ваш браузер не поддерживает аудио.
        </audio>
        <div className="flex justify-between items-center">
          <label htmlFor="startTime" className="text-white">
            Начало (сек):
          </label>
          <input
            id="startTime"
            type="number"
            className="p-2 rounded bg-neutral-700 text-white"
            value={startTime}
            onChange={(e) => setStartTime(Number(e.target.value))}
            min={0}
          />
        </div>
        <div className="flex justify-between items-center">
          <label htmlFor="endTime" className="text-white">
            Конец (сек):
          </label>
          <input
            id="endTime"
            type="number"
            className="p-2 rounded bg-neutral-700 text-white"
            value={endTime}
            onChange={(e) => setEndTime(Number(e.target.value))}
            min={0}
          />
        </div>
        <button
          onClick={handleCut}
          className="bg-blue-600 hover:bg-blue-500 text-white py-2 px-4 rounded disabled:opacity-50"
          disabled={isProcessing}
        >
          {isProcessing ? "Обработка..." : "Обрезать"}
        </button>
        {downloadLink && (
          <a
            href={downloadLink}
            download={`${song.title}_clip.mp3`}
            className="bg-green-600 hover:bg-green-500 text-white py-2 px-4 rounded text-center"
          >
            Скачать вырезанный фрагмент
          </a>
        )}
      </div>
    </Modal>
  );
};

export default AudioCutterModal;