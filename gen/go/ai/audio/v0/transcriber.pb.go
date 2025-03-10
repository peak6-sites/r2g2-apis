// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.33.0
// 	protoc        (unknown)
// source: ai/audio/v0/transcriber.proto

// buf:lint:ignore PACKAGE_VERSION_SUFFIX

package audiopb

import (
	_ "buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go/buf/validate"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// Request to `Transcribe`.
type TranscribeRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// REQUIRED. Data sources of audio file to transcribe.
	//
	// Types that are assignable to Data:
	//
	//	*TranscribeRequest_InlineData
	//	*TranscribeRequest_FileData
	Data isTranscribeRequest_Data `protobuf_oneof:"data"`
	// OPTIONAL. Instructions to guide the model on the style of produced output text.
	Prompt string `protobuf:"bytes,4,opt,name=prompt,proto3" json:"prompt,omitempty"`
}

func (x *TranscribeRequest) Reset() {
	*x = TranscribeRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_ai_audio_v0_transcriber_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TranscribeRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TranscribeRequest) ProtoMessage() {}

func (x *TranscribeRequest) ProtoReflect() protoreflect.Message {
	mi := &file_ai_audio_v0_transcriber_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TranscribeRequest.ProtoReflect.Descriptor instead.
func (*TranscribeRequest) Descriptor() ([]byte, []int) {
	return file_ai_audio_v0_transcriber_proto_rawDescGZIP(), []int{0}
}

func (m *TranscribeRequest) GetData() isTranscribeRequest_Data {
	if m != nil {
		return m.Data
	}
	return nil
}

func (x *TranscribeRequest) GetInlineData() *Blob {
	if x, ok := x.GetData().(*TranscribeRequest_InlineData); ok {
		return x.InlineData
	}
	return nil
}

func (x *TranscribeRequest) GetFileData() *FileData {
	if x, ok := x.GetData().(*TranscribeRequest_FileData); ok {
		return x.FileData
	}
	return nil
}

func (x *TranscribeRequest) GetPrompt() string {
	if x != nil {
		return x.Prompt
	}
	return ""
}

type isTranscribeRequest_Data interface {
	isTranscribeRequest_Data()
}

type TranscribeRequest_InlineData struct {
	InlineData *Blob `protobuf:"bytes,1,opt,name=inline_data,json=inlineData,proto3,oneof"`
}

type TranscribeRequest_FileData struct {
	FileData *FileData `protobuf:"bytes,2,opt,name=file_data,json=fileData,proto3,oneof"`
}

func (*TranscribeRequest_InlineData) isTranscribeRequest_Data() {}

func (*TranscribeRequest_FileData) isTranscribeRequest_Data() {}

// Raw binary data.
type Blob struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// REQUIRED. The IANA standard MIME type of the source data.
	MimeType string `protobuf:"bytes,1,opt,name=mime_type,json=mimeType,proto3" json:"mime_type,omitempty"`
	// REQUIRED. Binary data.
	Data []byte `protobuf:"bytes,2,opt,name=data,proto3" json:"data,omitempty"`
}

func (x *Blob) Reset() {
	*x = Blob{}
	if protoimpl.UnsafeEnabled {
		mi := &file_ai_audio_v0_transcriber_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Blob) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Blob) ProtoMessage() {}

func (x *Blob) ProtoReflect() protoreflect.Message {
	mi := &file_ai_audio_v0_transcriber_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Blob.ProtoReflect.Descriptor instead.
func (*Blob) Descriptor() ([]byte, []int) {
	return file_ai_audio_v0_transcriber_proto_rawDescGZIP(), []int{1}
}

func (x *Blob) GetMimeType() string {
	if x != nil {
		return x.MimeType
	}
	return ""
}

func (x *Blob) GetData() []byte {
	if x != nil {
		return x.Data
	}
	return nil
}

// Reference to a remote file.
type FileData struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// REQUIRED. The IANA standard MIME type of the source data.
	MimeType string `protobuf:"bytes,1,opt,name=mime_type,json=mimeType,proto3" json:"mime_type,omitempty"`
	// REQUIRED. URI of the remote file.
	// The following URI formats are supported:
	// - An unauthenticated HTTP URI.
	// - Google Cloud Storage URI in the form `gs://<bucket>/<object>`. When providing a URI to Google Cloud Storage,
	// the bucket must be public or access must be granted to the Service Account for the audio-server.
	Uri string `protobuf:"bytes,2,opt,name=uri,proto3" json:"uri,omitempty"`
}

func (x *FileData) Reset() {
	*x = FileData{}
	if protoimpl.UnsafeEnabled {
		mi := &file_ai_audio_v0_transcriber_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FileData) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FileData) ProtoMessage() {}

func (x *FileData) ProtoReflect() protoreflect.Message {
	mi := &file_ai_audio_v0_transcriber_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FileData.ProtoReflect.Descriptor instead.
func (*FileData) Descriptor() ([]byte, []int) {
	return file_ai_audio_v0_transcriber_proto_rawDescGZIP(), []int{2}
}

func (x *FileData) GetMimeType() string {
	if x != nil {
		return x.MimeType
	}
	return ""
}

func (x *FileData) GetUri() string {
	if x != nil {
		return x.Uri
	}
	return ""
}

// Transcribed audio.
type Transcription struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The transcribed text.
	Text string `protobuf:"bytes,1,opt,name=text,proto3" json:"text,omitempty"`
}

func (x *Transcription) Reset() {
	*x = Transcription{}
	if protoimpl.UnsafeEnabled {
		mi := &file_ai_audio_v0_transcriber_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Transcription) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Transcription) ProtoMessage() {}

func (x *Transcription) ProtoReflect() protoreflect.Message {
	mi := &file_ai_audio_v0_transcriber_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Transcription.ProtoReflect.Descriptor instead.
func (*Transcription) Descriptor() ([]byte, []int) {
	return file_ai_audio_v0_transcriber_proto_rawDescGZIP(), []int{3}
}

func (x *Transcription) GetText() string {
	if x != nil {
		return x.Text
	}
	return ""
}

var File_ai_audio_v0_transcriber_proto protoreflect.FileDescriptor

var file_ai_audio_v0_transcriber_proto_rawDesc = []byte{
	0x0a, 0x1d, 0x61, 0x69, 0x2f, 0x61, 0x75, 0x64, 0x69, 0x6f, 0x2f, 0x76, 0x30, 0x2f, 0x74, 0x72,
	0x61, 0x6e, 0x73, 0x63, 0x72, 0x69, 0x62, 0x65, 0x72, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12,
	0x0b, 0x61, 0x69, 0x2e, 0x61, 0x75, 0x64, 0x69, 0x6f, 0x2e, 0x76, 0x30, 0x1a, 0x1b, 0x62, 0x75,
	0x66, 0x2f, 0x76, 0x61, 0x6c, 0x69, 0x64, 0x61, 0x74, 0x65, 0x2f, 0x76, 0x61, 0x6c, 0x69, 0x64,
	0x61, 0x74, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xac, 0x01, 0x0a, 0x11, 0x54, 0x72,
	0x61, 0x6e, 0x73, 0x63, 0x72, 0x69, 0x62, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12,
	0x34, 0x0a, 0x0b, 0x69, 0x6e, 0x6c, 0x69, 0x6e, 0x65, 0x5f, 0x64, 0x61, 0x74, 0x61, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x11, 0x2e, 0x61, 0x69, 0x2e, 0x61, 0x75, 0x64, 0x69, 0x6f, 0x2e,
	0x76, 0x30, 0x2e, 0x42, 0x6c, 0x6f, 0x62, 0x48, 0x00, 0x52, 0x0a, 0x69, 0x6e, 0x6c, 0x69, 0x6e,
	0x65, 0x44, 0x61, 0x74, 0x61, 0x12, 0x34, 0x0a, 0x09, 0x66, 0x69, 0x6c, 0x65, 0x5f, 0x64, 0x61,
	0x74, 0x61, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x15, 0x2e, 0x61, 0x69, 0x2e, 0x61, 0x75,
	0x64, 0x69, 0x6f, 0x2e, 0x76, 0x30, 0x2e, 0x46, 0x69, 0x6c, 0x65, 0x44, 0x61, 0x74, 0x61, 0x48,
	0x00, 0x52, 0x08, 0x66, 0x69, 0x6c, 0x65, 0x44, 0x61, 0x74, 0x61, 0x12, 0x16, 0x0a, 0x06, 0x70,
	0x72, 0x6f, 0x6d, 0x70, 0x74, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x70, 0x72, 0x6f,
	0x6d, 0x70, 0x74, 0x42, 0x0d, 0x0a, 0x04, 0x64, 0x61, 0x74, 0x61, 0x12, 0x05, 0xba, 0x48, 0x02,
	0x08, 0x01, 0x4a, 0x04, 0x08, 0x03, 0x10, 0x04, 0x22, 0x37, 0x0a, 0x04, 0x42, 0x6c, 0x6f, 0x62,
	0x12, 0x1b, 0x0a, 0x09, 0x6d, 0x69, 0x6d, 0x65, 0x5f, 0x74, 0x79, 0x70, 0x65, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x08, 0x6d, 0x69, 0x6d, 0x65, 0x54, 0x79, 0x70, 0x65, 0x12, 0x12, 0x0a,
	0x04, 0x64, 0x61, 0x74, 0x61, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0c, 0x52, 0x04, 0x64, 0x61, 0x74,
	0x61, 0x22, 0x39, 0x0a, 0x08, 0x46, 0x69, 0x6c, 0x65, 0x44, 0x61, 0x74, 0x61, 0x12, 0x1b, 0x0a,
	0x09, 0x6d, 0x69, 0x6d, 0x65, 0x5f, 0x74, 0x79, 0x70, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x08, 0x6d, 0x69, 0x6d, 0x65, 0x54, 0x79, 0x70, 0x65, 0x12, 0x10, 0x0a, 0x03, 0x75, 0x72,
	0x69, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x75, 0x72, 0x69, 0x22, 0x23, 0x0a, 0x0d,
	0x54, 0x72, 0x61, 0x6e, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x12, 0x0a,
	0x04, 0x74, 0x65, 0x78, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x74, 0x65, 0x78,
	0x74, 0x32, 0x59, 0x0a, 0x0b, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x63, 0x72, 0x69, 0x62, 0x65, 0x72,
	0x12, 0x4a, 0x0a, 0x0a, 0x54, 0x72, 0x61, 0x6e, 0x73, 0x63, 0x72, 0x69, 0x62, 0x65, 0x12, 0x1e,
	0x2e, 0x61, 0x69, 0x2e, 0x61, 0x75, 0x64, 0x69, 0x6f, 0x2e, 0x76, 0x30, 0x2e, 0x54, 0x72, 0x61,
	0x6e, 0x73, 0x63, 0x72, 0x69, 0x62, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x1a,
	0x2e, 0x61, 0x69, 0x2e, 0x61, 0x75, 0x64, 0x69, 0x6f, 0x2e, 0x76, 0x30, 0x2e, 0x54, 0x72, 0x61,
	0x6e, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x22, 0x00, 0x42, 0x3d, 0x5a, 0x3b,
	0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x70, 0x65, 0x61, 0x6b, 0x36,
	0x2d, 0x73, 0x69, 0x74, 0x65, 0x73, 0x2f, 0x72, 0x32, 0x67, 0x32, 0x2d, 0x61, 0x70, 0x69, 0x73,
	0x2f, 0x67, 0x65, 0x6e, 0x2f, 0x67, 0x6f, 0x2f, 0x61, 0x69, 0x2f, 0x61, 0x75, 0x64, 0x69, 0x6f,
	0x2f, 0x76, 0x30, 0x3b, 0x61, 0x75, 0x64, 0x69, 0x6f, 0x70, 0x62, 0x62, 0x06, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x33,
}

var (
	file_ai_audio_v0_transcriber_proto_rawDescOnce sync.Once
	file_ai_audio_v0_transcriber_proto_rawDescData = file_ai_audio_v0_transcriber_proto_rawDesc
)

func file_ai_audio_v0_transcriber_proto_rawDescGZIP() []byte {
	file_ai_audio_v0_transcriber_proto_rawDescOnce.Do(func() {
		file_ai_audio_v0_transcriber_proto_rawDescData = protoimpl.X.CompressGZIP(file_ai_audio_v0_transcriber_proto_rawDescData)
	})
	return file_ai_audio_v0_transcriber_proto_rawDescData
}

var file_ai_audio_v0_transcriber_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_ai_audio_v0_transcriber_proto_goTypes = []interface{}{
	(*TranscribeRequest)(nil), // 0: ai.audio.v0.TranscribeRequest
	(*Blob)(nil),              // 1: ai.audio.v0.Blob
	(*FileData)(nil),          // 2: ai.audio.v0.FileData
	(*Transcription)(nil),     // 3: ai.audio.v0.Transcription
}
var file_ai_audio_v0_transcriber_proto_depIdxs = []int32{
	1, // 0: ai.audio.v0.TranscribeRequest.inline_data:type_name -> ai.audio.v0.Blob
	2, // 1: ai.audio.v0.TranscribeRequest.file_data:type_name -> ai.audio.v0.FileData
	0, // 2: ai.audio.v0.Transcriber.Transcribe:input_type -> ai.audio.v0.TranscribeRequest
	3, // 3: ai.audio.v0.Transcriber.Transcribe:output_type -> ai.audio.v0.Transcription
	3, // [3:4] is the sub-list for method output_type
	2, // [2:3] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_ai_audio_v0_transcriber_proto_init() }
func file_ai_audio_v0_transcriber_proto_init() {
	if File_ai_audio_v0_transcriber_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_ai_audio_v0_transcriber_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TranscribeRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_ai_audio_v0_transcriber_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Blob); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_ai_audio_v0_transcriber_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FileData); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_ai_audio_v0_transcriber_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Transcription); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	file_ai_audio_v0_transcriber_proto_msgTypes[0].OneofWrappers = []interface{}{
		(*TranscribeRequest_InlineData)(nil),
		(*TranscribeRequest_FileData)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_ai_audio_v0_transcriber_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_ai_audio_v0_transcriber_proto_goTypes,
		DependencyIndexes: file_ai_audio_v0_transcriber_proto_depIdxs,
		MessageInfos:      file_ai_audio_v0_transcriber_proto_msgTypes,
	}.Build()
	File_ai_audio_v0_transcriber_proto = out.File
	file_ai_audio_v0_transcriber_proto_rawDesc = nil
	file_ai_audio_v0_transcriber_proto_goTypes = nil
	file_ai_audio_v0_transcriber_proto_depIdxs = nil
}
